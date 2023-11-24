import tkinter as tk

from gui import UncheckedList


if __name__ == '__main__':
    root = tk.Tk()
    app = UncheckedList('header', master=root)
    root.title(u"所見未確認リスト")
    root.geometry("480x240")
    csv_path = app.csv_path
    root.mainloop()
