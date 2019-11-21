import tkinter
import credientials
import datetime
import final
from tkinter import *
import details
def show(x,y,z,q):
    print(x)
    array=x
    self=Tk()
    self.geometry('400x450')
    self.wm_title('Enter Details')
    self.config(background='grey')
    client=credientials.client
    db=client.test
    x=Label(self,text="Please Enter User Information To Generate Booking Id",bg='white').place(x=40,y=180,height=15,width=350)
    x=Label(self,text="NAME:",bg='white').place(x=10,y=250,height=20,width=100)
    x=Label(self,text="EMAIL:",bg='white').place(x=10,y=300,height=20,width=100)
    x=Label(self,text="MOBILE NUMBER:",bg='white').place(x=10,y=350,height=20,width=100)
    a1=StringVar()
    a2=StringVar()
    a3=StringVar()
       
    e1=Entry(self,textvariable=a1).place(x=140,y=250,height=20,width=170)
    e2=Entry(self,textvariable=a2).place(x=140,y=300,height=20,width=170)
    e3=Entry(self,textvariable=a3).place(x=140,y=350,height=20,width=170)
    def confirm():
        name=a1.get()
        email=a2.get()
        phone=a3.get()
        db.M1S1.update({'id':y['id']},{'id':y['id'],'M1S1':array,'Time':y['Time'],'Show':y['Show'],'Movie':y['Movie']})
        result=db.userdata.insert_one({'Name':name,'Email':email,'Phone':phone,'date':datetime.datetime.utcnow(),'Time':y['Time'],'Movie':y['Show'],'Srno':z,'Stno':q})
        self.destroy()
        yy=db.userdata.find_one({'Name':name})
        final.enter(yy['_id'])

    b1=Button(self,text='Confirm',bg="white",command=lambda:confirm())
    b1.place(x=80,y=405,height=35,width=90)
   
    b2=Button(self,text='Cancel',bg="white",command=lambda:self.destroy())
    b2.place(x=230,y=405,height=35,width=90)

    self.mainloop()
