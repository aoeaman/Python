import tkinter
from tkinter import *
import xyz
from PIL import ImageTk
from PIL import Image
def enter(q):
    master=Tk()
    master.geometry('400x450')
    master.config(background='white')

    render=ImageTk.PhotoImage(Image.open('xyz.jpg'))
    img=Label(master,image=render)
    img.image=render
    img.place(x=0,y=0,height=200,width=400)
   

    def confirm():
        master.destroy()
        xyz.show(q[7],q[6],q[1],q[3])

    
  


    x1=Label(master,text="TICKETS:",bg='#66a3ff').place(x=10,y=240,height=20,width=60)
    x2=Label(master,text="SEAT NUMBER:",bg='#66a3ff').place(x=10,y=270,height=20,width=85)
    x3=Label(master,text="SHOW TIME:",bg='#66a3ff').place(x=10,y=300,height=20,width=80)
    x4=Label(master,text="SCREEN NUMBER:",bg='#66a3ff').place(x=10,y=330,height=20,width=100)
    x5=Label(master,text="TOTAL PRICE:",bg='#66a3ff').place(x=10,y=360,height=20,width=85)
    if q[0]>=2:
        q[4]=q[4]-100
        x10=Label(master,text="CENIMA100 Aplied!!!!",bg='#66a3ff',font='verdana 8').place(x=205,y=360,height=20,width=150)

    x1=Label(master,text=q[0],bg='#66a3ff').place(x=120,y=240,height=20,width=95)
    x2=Label(master,text=q[1],bg='#66a3ff').place(x=120,y=270,height=20,width=90)
    x3=Label(master,text=q[2],bg='#66a3ff').place(x=120,y=300,height=20,width=80)
    x4=Label(master,text=q[3],bg='#66a3ff').place(x=120,y=330,height=20,width=80)
    x5=Label(master,text=q[4],bg='#66a3ff').place(x=120,y=360,height=20,width=85)
    

    x6=Label(master,text="Show: ",bg='#66a3ff').place(x=10,y=210,height=20,width=70)
    x6=Label(master,text=q[5],bg='#66a3ff').place(x=120,y=210,height=20,width=180)

    b1=Button(master,text='Book Now',bg="white",command=lambda:confirm())
    b1.place(x=80,y=405,height=35,width=90)
   
    b2=Button(master,text='Cancel',bg="white",command=lambda:master.destroy())
    b2.place(x=230,y=405,height=35,width=90)

    master.mainloop()
