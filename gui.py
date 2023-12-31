import os.path
import sys
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox

import handlefile
from handleexcel import set_styles
from manage_examlist import get_unchecked_table, get_departments_from_df


class UncheckedList(tk.Frame):

    def __init__(self, header_path, master=None):
        super().__init__(master)
        #TODO: 現在のディレクトリを登録
        #TODO: このディレクトリに基づいてheaderファイルを読み込む。
        self.current_dir = sys.argv[0]
        self.file_path = ""
        self.excel_path = ""
        self.header_path = header_path
        self.frame = tk.Frame(master)
        self.frame.pack()
        self.label_frame = None
        self.csv_entry = None
        self.browse_button = None
        self.start_button = None
        self.pack()
        self.set_ui()

    def set_ui(self):
        self.label_frame = tk.LabelFrame(self.frame, text='csvファイル')
        self.label_frame.grid(row=0, column=0, sticky="news", padx=10, pady=10)

        self.csv_entry = tk.Entry(self.label_frame)
        self.csv_entry.grid(row=0, column=0)

        self.browse_button = tk.Button(self.label_frame, text="Browse", command=self.filedialog_open)
        self.browse_button.grid(row=0, column=1)

        self.start_button = tk.Button(self, text="Start", command=self.output_unchecked_list)
        self.start_button.grid(row=1, column=1)

    def filedialog_open(self):
        file_path = tk.filedialog.askopenfilename(
            title='csvファイルを指定してください',
            filetypes=[("CSV ファイル", ".csv")],
            initialdir='./'
        )
        self.csv_entry.delete(0, tk.END)
        self.csv_entry.insert(0, file_path)
        print(self.csv_path)

    @property
    def csv_path(self):
        return self.csv_entry.get()

    def get_excel_path(self):
        base_name = os.path.basename(self.csv_path)
        file_name_without_ext, _ = os.path.splitext(base_name)
        return file_name_without_ext + ".xlsx"

    def validate_input_file(self):
        if not os.path.exists(self.csv_path):
            tk.messagebox.showinfo("", "ファイルが見つかりません。\n{}".format(self.csv_path))
            return False

        with open(self.csv_path, 'r', encoding='utf-8') as file:
            try:
                file.read(100)
            except UnicodeDecodeError:
                handlefile.sjis_to_utf8(self.csv_path)
                print("ファイルの文字コード変換")
        return True

    def output_unchecked_list(self):
        if not self.validate_input_file():
            return
        self.excel_path = self.get_excel_path()
        unchecked_table = get_unchecked_table(self.csv_path, self.header_path, sort=True)
        print('診療科取得')
        departments = get_departments_from_df(unchecked_table)
        print('診療科取得完了')

        print('excelに保存する')
        handlefile.write_excel(self.excel_path, unchecked_table, departments)
        print('excelに保存完了.\n{}'.format(self.excel_path))
        wb = handlefile.open_excel(self.excel_path)
        print('Style 適用')
        set_styles(wb, self.excel_path)
        print('保存完了')
