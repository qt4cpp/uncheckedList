import os.path
import tkinter as tk
import tkinter.filedialog

import handlefile
from handleexcel import set_styles
from manage_examlist import get_unchecked_table, get_departments_from_df


class UncheckedList(tk.Frame):

    def __init__(self, header_path, master=None):
        super().__init__(master)
        self.file_path = ""
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

    def output_unchecked_list(self):
        unchecked_table = get_unchecked_table(self.csv_path, self.header_path, sort=True)
        print('診療科取得')
        departments = get_departments_from_df(unchecked_table)
        print('診療科取得完了')

        print('excelに保存する')
        handlefile.write_excel('test.xlsx', unchecked_table, departments)
        print('excelに保存完了')
        wb = handlefile.open_excel('test.xlsx')
        set_styles(wb)

