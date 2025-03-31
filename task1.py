import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title('tk')
window.geometry("500x50")
f = Frame()
entry1 = Entry(f)
label1 = Label(f, text='x')
entry2 = Entry(f)
label2 = Button(f, text='=')
entry3 = Entry(f, text='')

f.pack()

entry1.pack(side=LEFT)
label1.pack(side=LEFT)
entry2.pack(side=LEFT)
label2.pack(side=LEFT)
entry3.pack(side=LEFT)


window.mainloop()

#done