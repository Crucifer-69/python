from tkinter import *
from tkinter import ttk

root = Tk()
entry = ttk.Entry(root, width=25)
entry.pack()
button = ttk.Button(root, text="click me")
button.pack()
style = ttk.Style()
style.configure('TButton',background='red')

def BuClick():
    print(entry.get())
    var=StringVar()
    label = Label(root, textvariable=var)
    var.set(entry.get())
    label.pack()
    entry.delete(0, END)
button.config(command=BuClick)

root.mainloop()
