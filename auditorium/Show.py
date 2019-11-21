import main
from tkinter import *
import credientials
from bson.objectid import ObjectId
from PIL import *
def show(iid):
    def back():
        self.destroy()
        main.ada()
    self=Tk()
    self.geometry("400x600")
    client=credientials.client
    db=client.test
    info=db.userdata.find({'_id':ObjectId(iid)})[0]
    self.config(background='white')
    render=ImageTk.PhotoImage(Image.open('myticket1.jpg'))
    img=Label(self,image=render)
    img.image=render
    img.place(x=0,y=0)

    b5=Button(self,text="B A C K",bg='black',fg='white',command=lambda:back())
    b5.place(bordermode=INSIDE,x=320,y=490,height=20,width=70)

    x=Label(self,text="NAME:",bg='white',anchor=W).place(x=10,y=250,height=15,width=120)
    x=Label(self,text="EMAIL:",bg='white',anchor=W).place(x=10,y=280,height=15,width=120)
    x=Label(self,text="MOBILE NUMBER:",bg='white',anchor=W).place(x=10,y=310,height=15,width=120)
    x=Label(self,text="NUMBER OF TICKETS",bg='white',anchor=W).place(x=10,y=340,height=15,width=120)
    x=Label(self,text="SEAT NUMBER:",bg='white',anchor=W).place(x=10,y=370,height=15,width=120)
    x=Label(self,text="SHOW TIME:",bg='white',anchor=W).place(x=10,y=400,height=15,width=120)
    x=Label(self,text="SCREEN NUMBER",bg='white',anchor=W).place(x=10,y=430,height=15,width=120)
    x=Label(self,text="SELECTED SHOW:",bg='white',anchor=W).place(x=10,y=460,height=15,width=120)
    x=Label(self,text="TOTAL PRICE:",bg='white',anchor=W).place(x=10,y=490,height=15,width=120)

    if len(info['Srno'])>=2:
        price=len(info['Srno'])*200-100
    else:
        price=len(info['Srno'])*200
    x=Label(self,text=info['Name'],bg='white',anchor=W).place(x=150,y=250,height=15,width=150)
    x=Label(self,text=info['Email'],bg='white',anchor=W).place(x=150,y=280,height=15,width=190)
    x=Label(self,text=info['Phone'],bg='white',anchor=W).place(x=150,y=310,height=15,width=110)
    x=Label(self,text=len(info['Srno']),bg='white',anchor=W).place(x=150,y=340,height=15,width=150)
    x=Label(self,text=info['Srno'],bg='white',anchor=W).place(x=150,y=370,height=15,width=150)
    x=Label(self,text=info['Time'],bg='white',anchor=W).place(x=150,y=400,height=15,width=150)
    x=Label(self,text=info['Stno'],bg='white',anchor=W).place(x=150,y=430,height=15,width=150)
    x=Label(self,text=info['Movie'],bg='white',anchor=W).place(x=150,y=460,height=15,width=200)
    x=Label(self,text=price,bg='white',anchor=W).place(x=150,y=490,height=15,width=150)
    
    
    self.mainloop()
