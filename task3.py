import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Example")
dogpic = PhotoImage(file="dog.png")

dogpiclbl = tk.Label(window, image=dogpic)
titlelbl = tk.Label(window, text="Pochacco!")
textlbl = tk.Label(window, text="A cuddly little puppy! This is from the same\ncreators who brought you Keropi and Kero Kero", bg="#96f8ff")

dogpiclbl.grid(row=1,column=2)
titlelbl.grid(row=1,column=3)
textlbl.grid(row=2,column=1, columnspan=4)

window.mainloop()

#done