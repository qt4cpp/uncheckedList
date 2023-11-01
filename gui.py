import os.path
import tkinter as tk
import tkinter.filedialog


class UncheckedList(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.file_path = ""
        self.frame = tk.Frame(master)
        self.frame.pack()
        self.label_frame = None
        self.csv_entry = None
        self.browse_button = None
        self.pack()
        self.set_ui()

    def set_ui(self):
        self.label_frame = tk.LabelFrame(self.frame, text='csvファイル')
        self.label_frame.grid(row=0, column=0, sticky="news", padx=10, pady=10)
        # self.label = tk.Label(self, text="csvファイルを指定してください。")
        # self.label.pack()

        self.csv_entry = tk.Entry(self.label_frame)
        self.csv_entry.grid(row=0, column=0)

        self.browse_button = tk.Button(self.label_frame, text="Browse", command=self.filedialog_open)
        self.browse_button.grid(row=0, column=1)

    def filedialog_open(self):
        file_path = tk.filedialog.askopenfilename(
            title='csvファイルを指定してください',
            filetypes=[("CSV ファイル", ".csv")],
            initialdir='./'
        )
        self.csv_entry.delete(0, tk.END)
        self.csv_entry.insert(0, file_path)


root = tk.Tk()
app = UncheckedList(master=root)
root.title(u"未読影リスト")
root.geometry("480x220")
root.mainloop()
