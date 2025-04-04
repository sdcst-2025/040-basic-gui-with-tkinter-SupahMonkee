import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title('T-Town Veterinary Clinic Database')
dogpic = PhotoImage(file='dog.png')

piclbl = tk.Label(window, image=dogpic, borderwidth=3)
button1 = tk.Button(window, text="Search by Name")
entry1 = tk.Entry(window)
titlelbl = tk.Label(window, text="Client Database")
namelbl = tk.Label(window, text="Name")
typelbl = tk.Label(window, text="Type")
breedlbl = tk.Label(window, text="Breed")
ownerlbl = tk.Label(window, text="Owner")
birthdatelbl = tk.Label(window, text="Birthdate")
nameent = tk.Entry(window)
typeent = tk.Entry(window)
breedent = tk.Entry(window)
ownerent = tk.Entry(window)
birthdateent = tk.Entry(window)
prevbutt = tk.Button(window, text="< Previous")
savebutt = tk.Button(window, text="Save Entry")
nextbutt = tk.Button(window, text="Next >")



piclbl.grid(row=1, column=1, rowspan=2)
button1.grid(row=1, column=4)
entry1.grid(row=1, column=5)
titlelbl.grid(row=1, column=3, rowspan=2)
namelbl.grid(row=3,column=1)
nameent.grid(row=4,column=1)
typelbl.grid(row=3,column=2)
typeent.grid(row=4,column=2)
breedlbl.grid(row=3,column=3)
breedent.grid(row=4,column=3)
ownerlbl.grid(row=3,column=4)
ownerent.grid(row=4,column=4)
birthdatelbl.grid(row=3,column=5)
birthdateent.grid(row=4,column=5)
prevbutt.grid(row=5, column=1)
savebutt.grid(row=5, column=3)
nextbutt.grid(row=5,column=5)


window.mainloop()

#done