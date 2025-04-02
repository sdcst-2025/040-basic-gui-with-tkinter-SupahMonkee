import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title('Example')
window.geometry('260x135')
dogpic = PhotoImage(file='dog.png')

doglbl = tk.Label(window, image=dogpic)
titlelbl = tk.Label(window, text='Pochacco!')
textlbl = tk.Label(window, text='A cuddly little puppy! This is from the same\n creators who brought you Keropi and Kero Kero', bg="#96f8ff")

doglbl.place(x=50,y=0)
titlelbl.place(x=125,y=40)
textlbl.place(x=0,y=100)

window.mainloop()

#done