from tkinter import *
import tkinter.messagebox as tkmb
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.geometry("600x900")
root.title("Classes but it is on a root window")
root.configure(background="lavender")
wobjects = ("textbox","button","image")

class createobj:
    def __init__(self):
        print("I HAVE BEEN CREATED")
    def addstuff(self):
        label = Label(root, text="This was created using classes, how amazing, and it is also white so wow", bg="violet",fg="white")
        label.pack()
    def clickme(self):
        tkmb.showinfo("Epicc Textbox","You just saw an epicc textbox")
    def addmorestuff(self):
        btn = Button(root, text="click me for epicc", command=self.clickme)
        btn.pack(padx=20,pady=10)
    def addevenmorestuff(self):
        hi = ImageTk.PhotoImage(Image.open("smthing.png"))
        imag=Label(root)
        imag["image"]=hi
        imag.pack()

def ae():
    val = dropdown.get()
    if(val == "textbox"):
        objecc.addstuff()
    elif(val=="button"):
        objecc.addmorestuff()
    elif(val=="image"):
        objecc.addevenmorestuff()

objecc = createobj()
dropdown=ttk.Combobox(root, state="readonly", values=wobjects)
dropdown.pack()
bttn = Button(root, text="click me to create new and epicc gui", command=ae)
bttn.pack(padx=20,pady=10)

root.mainloop()