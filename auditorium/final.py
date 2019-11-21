import tkinter
import os
import main
import pyperclip
from tkinter import *
from PIL import ImageTk
from PIL import Image
def enter(iid):
    def home():
        pyperclip.copy(str(iid))
        master.destroy()
        main.ada()
    master=Tk()
    master.geometry('400x450')
    master.config(background='white')

    render=ImageTk.PhotoImage(Image.open('xyz.jpg'))
    img=Label(master,image=render)
    img.image=render
    xy=Button(master,text="Home",command=lambda:home()).place(x=10,y=320,height=20,width=150)
    img.place(x=0,y=0,height=200,width=400)
    xy=Label(master,text="Booking Confirmed!").place(x=10,y=200,height=20,width=150)
    xz=Entry(master)
    xz.place(x=100,y=270,height=20,width=200)
    xz.insert(END,iid)
    
   
    master.mainloop()
