import tkinter as tk
import tkinter.filedialog


class UncheckedList(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.label = None
        self.entry = None
        self.button = None
        self.pack()
        self.set_ui()

    def set_ui(self):
        self.label = tk.Label(self, text="csvファイルを指定してください。")
        self.label.pack()

        self.entry = tk.Entry(self)
        self.entry.pack(side=tk.LEFT)

        self.button = tk.Button(self, text="Browse", command=self.filedialog_open)
        self.button.pack(side=tk.RIGHT)

    def filedialog_open(self):
        file_path = tk.filedialog.askopenfilename(
            title='csvファイルを指定してください',
            filetypes=[("CSV ファイル", ".csv")],
            initialdir='./'
        )
        self.entry.delete(0, tk.END)
        self.entry.insert(0, file_path)


root = tk.Tk()

app = UncheckedList(master=root)
root.title(u"未読影リスト")
root.geometry("320x120")
root.mainloop()
