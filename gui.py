import tkinter as tk
import tkinter.filedialog


def filedialog_open():
    file_path = tk.filedialog.askopenfilename(
        title='csvファイルを指定してください',
        filetypes=[("CSV ファイル", ".csv")],
        initialdir='./'
    )
    entry.delete(0, tk.END)
    entry.insert(0, file_path)


root = tk.Tk()
label = tk.Label(root, text="csvファイルを指定してください。")
label.pack()
entry = tk.Entry(root)
entry.pack(side=tk.LEFT)

button = tk.Button(root, text="Browse", command=filedialog_open)
button.pack(side=tk.RIGHT)

root.title(u"未読影リスト")
root.geometry("320x120")
root.mainloop()
