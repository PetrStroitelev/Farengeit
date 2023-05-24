from tkinter import *
from tkinter import ttk

def faringeite(*args):
    try:
        y = float(cel.get())
        far.set(y * 1.8 + 32)
    except ValueError:
        pass

root = Tk()
root.title('Фарингометр')

mainfraime = ttk.Frame(root, borderwidth=15)
mainfraime.grid()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
cel = StringVar()
cel_Entry = ttk.Entry(mainfraime, textvariable=cel)
cel_Entry.grid(column=1, row=0, sticky="EWNS")
ttk.Label(mainfraime, text='Введите температуру в Цельсиях: ', foreground='Black').grid(column=0, row=0, sticky="EWNS")


far = StringVar(value="В Фарингейтах получится...")
ttk.Label(mainfraime, relief="sunken", foreground='Blue', textvariable=far).grid(column=1, row=1, sticky="EWNS")
ttk.Label(mainfraime, text='Получится в Фаренгейтах: ', foreground='Black').grid(column=0, row=1, sticky="EWNS")


ttk.Button(mainfraime, text='Convert', command=faringeite).grid(columnspan=2, sticky="EW")

root.bind("<Return>", faringeite)
for child in mainfraime.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()