import handlefile
import tkinter as tk
from handleexcel import set_styles
from manage_examlist import get_departments_from_df, get_unchecked_table
from gui import UncheckedList


if __name__ == '__main__':
    root = tk.Tk()
    app = UncheckedList('header', master=root)
    root.title(u"所見未確認リスト")
    root.geometry("480x240")
    csv_path = app.csv_path
    root.mainloop()
