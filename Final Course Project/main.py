from tkinter import *

root = Tk()

# Create a lable widget and set its position on the screen
myLabel1 = Label(root, text="Hello, Medical User!")
myLabel2 = Label(root, text="Hello, Welcome to the app!")

myLabel1.grid(row=0, column=1)
myLabel2.grid(row=1, column=1)

doctorsCheckBtn = Button(root, text="View List of Doctors", padx=50)
patinetsCheckBtn = Button(root, text="View List of Patients", padx=50)
infoBtn = Button(root, text="About The App", padx=50)

doctorsCheckBtn.grid(row=2, column=1)
patinetsCheckBtn.grid(row=3, column=1)
infoBtn.grid(row=4, column=1)

root.mainloop()
