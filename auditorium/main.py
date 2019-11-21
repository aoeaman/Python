from tkinter import *
import tkinter as tk
from PIL import ImageTk
import credientials
from PIL import Image
import seats
import Show
def movieone(q):
    root.destroy()
    seats.lookup(q)
class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self,"SIP 4rd Sem")
        container=tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.geometry('400x480')
        self.config(background='red')
        self.resizable(False,False)
        self.frames={}
        global root
        root=self
        for F in (startpage,startpage1,movie1,movie2,movie3,movie4,myticketf,promocode,showtime):

            frame=F(container,self)
            self.frames[F]=frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(startpage)

    def show_frame(self,cont):
        frame=self.frames[cont]
        frame.tkraise()

class startpage(tk.Frame):
    def __init__(self,parant,controller):
        tk.Frame.__init__(self, parant)

        self.config(background='white')

        xx=Image.open('book.png')
        user1=ImageTk.PhotoImage(xx)

        xx=Image.open('myticket.jpg')
        user2=ImageTk.PhotoImage(xx)

        xx=Image.open('showtime.png')
        user3=ImageTk.PhotoImage(xx)

        xx=Image.open('discount.jpg')
        user4=ImageTk.PhotoImage(xx)
        
        
        b1=Button(self,image=user1,bg="#ccccff",command=lambda:controller.show_frame(startpage1))
        b1.place(x=20,y=240,height=50,width=110)
        b1.image=user1
        b2=Button(self,image=user2,bg="#ccccff",command=lambda:controller.show_frame(myticketf))
        b2.place(x=275,y=240,height=50,width=110)
        b2.image=user2
        b3=Button(self,image=user3,bg="#ccccff",command=lambda:controller.show_frame(showtime))
        b3.place(x=20,y=410,height=50,width=110)
        b3.image=user3
        b4=Button(self,image=user4,bg="#ccccff",command=lambda:controller.show_frame(promocode))
        b4.place(x=275,y=410,height=50,width=110)
        b4.image=user4

        render=ImageTk.PhotoImage(Image.open('myticket1.jpg'))
        img=Label(self,image=render)
        img.image=render
        img.place(x=0,y=0)

        render=ImageTk.PhotoImage(Image.open('cinema111.jpg'))
        img=Label(self,image=render)
        img.image=render
        img.place(x=120,y=290)
        
class startpage1(tk.Frame):
    def __init__(self,parant,controller):
        tk.Frame.__init__(self,parant)

        self.config(background='white')
         
        xx=Image.open('toh.jpg')
        user1=ImageTk.PhotoImage(xx)
        
        xx=Image.open('img2000.jpg')
        user2=ImageTk.PhotoImage(xx)
        
        xx=Image.open('avengers.jpg')
        user3=ImageTk.PhotoImage(xx)
        
        xx=Image.open('nun.jpg')
        user4=ImageTk.PhotoImage(xx)
        
        b1=Button(self,image=user1,command=lambda:controller.show_frame(movie1))
        b1.place(bordermode=INSIDE,x=10,y=10,height=200,width=180)
        b1.image=user1
        
        b2=Button(self,image=user2,command=lambda:controller.show_frame(movie2))
        b2.place(bordermode=INSIDE,x=210,y=10,height=200,width=180)
        b2.image=user2
        
        b3=Button(self,image=user3,command=lambda:controller.show_frame(movie3))
        b3.place(bordermode=INSIDE,x=10,y=230,height=200,width=180)
        b3.image=user3
        
        b4=Button(self,image=user4,command=lambda:controller.show_frame(movie4))
        b4.place(bordermode=INSIDE,x=210,y=230,height=200,width=180)
        b4.image=user4

        b5=Button(self,text="B A C K",bg='black',fg='white',command=lambda:controller.show_frame(startpage))
        b5.place(bordermode=INSIDE,x=300,y=440,height=30,width=70)

class movie1(tk.Frame):
    def __init__(self,parant,controller):
        tk.Frame.__init__(self,parant)


        self.config(background='#bfbfbf')


         
        render=ImageTk.PhotoImage(Image.open('hall.png'))
        img=Label(self,image=render)
        img.image=render
        img.place(x=0,y=0)
        
        
        x=Label(self,text="Screen 1").place(x=10,y=270,height=20,width=150)
        x=Label(self,text="Screen 2").place(x=200,y=270,height=20,width=150)
        
        b1=Button(self,text="9:00-11:50 AM",bg='#8c8c8c',fg='white',command=lambda:movieone(11))
        b1.place(bordermode=INSIDE,x=30,y=310,height=50,width=100)
        
        b2=Button(self,text="12:00-2:50 PM",bg='#8c8c8c',fg='white',command=lambda:movieone(12))
        b2.place(bordermode=INSIDE,x=220,y=310,height=50,width=100)


        b3=Button(self,text='B A C K',bg='white',command=lambda:controller.show_frame(startpage1))
        b3.place(bordermode=INSIDE,x=140,y=400,height=30,width=80)
        

class movie2(tk.Frame):
    def __init__(self,parant,controller):
        tk.Frame.__init__(self,parant)

        self.config(background='#bfbfbf')

        render=ImageTk.PhotoImage(Image.open('hall.png'))
        img=Label(self,image=render)
        img.image=render
        img.place(x=0,y=0)

        x=Label(self,text="Screen 1").place(x=10,y=270,height=20,width=150)
        x=Label(self,text="Screen 2").place(x=200,y=270,height=20,width=150)
        b1=Button(self,text="12:00-2:50 PM",bg='#8c8c8c',fg='white',command=lambda:movieone(21))
        b1.place(bordermode=INSIDE,x=30,y=310,height=50,width=100)
        
        b2=Button(self,text="9:00-11:50 AM",bg='#8c8c8c',fg='white',command=lambda:movieone(22))
        b2.place(bordermode=INSIDE,x=220,y=310,height=50,width=100)

        b3=Button(self,text="B A C K",command=lambda:controller.show_frame(startpage1))
        b3.place(bordermode=INSIDE,x=140,y=400,height=30,width=80)


class movie3(tk.Frame):
    def __init__(self,parant,controller):
        tk.Frame.__init__(self,parant)

        self.config(background='#bfbfbf')

        render=ImageTk.PhotoImage(Image.open('hall.png'))
        img=Label(self,image=render)
        img.image=render
        img.place(x=0,y=0)
        x=Label(self,text="Screen 1").place(x=10,y=270,height=20,width=150)
        x=Label(self,text="Screen 2").place(x=200,y=270,height=20,width=150)
        
        b1=Button(self,text="3:00-5:50 PM",bg='#8c8c8c',fg='white',command=lambda:movieone(31))
        b1.place(bordermode=INSIDE,x=30,y=310,height=50,width=100)
        
        b2=Button(self,text="6:00-8:50 PM",bg='#8c8c8c',fg='white',command=lambda:movieone(32))
        b2.place(bordermode=INSIDE,x=220,y=310,height=50,width=100)

        b3=Button(self,text="B A C K",command=lambda:controller.show_frame(startpage1))
        b3.place(bordermode=INSIDE,x=140,y=400,height=30,width=80)


class movie4(tk.Frame):
    def __init__(self,parant,controller):
        tk.Frame.__init__(self,parant)

        self.config(background='#bfbfbf')

        render=ImageTk.PhotoImage(Image.open('hall.png'))
        img=Label(self,image=render)
        img.image=render
        img.place(x=0,y=0)

        x=Label(self,text="Screen 1").place(x=10,y=270,height=20,width=150)
        x=Label(self,text="Screen 2").place(x=200,y=270,height=20,width=150)
        b1=Button(self,text="6:00-8:50 PM",bg='#8c8c8c',fg='white',command=lambda:movieone(41))
        b1.place(bordermode=INSIDE,x=30,y=310,height=50,width=100)
        
        b2=Button(self,text="3:00-5:50 PM",bg='#8c8c8c',fg='white',command=lambda:movieone(42))
        b2.place(bordermode=INSIDE,x=220,y=310,height=50,width=100)

        b3=Button(self,text="B A C K",command=lambda:controller.show_frame(startpage1))
        b3.place(bordermode=INSIDE,x=140,y=400,height=30,width=80)
class myticketf(tk.Frame):
     def __init__(self,parant,controller):
        def go():
             iid=E.get()
             root.destroy()
             Show.show(iid)
             
        tk.Frame.__init__(self,parant)
        self.config(background='white')
        render=ImageTk.PhotoImage(Image.open('myticket1.jpg'))
        img=Label(self,image=render)
        img.image=render
        img.place(x=0,y=0)

        b5=Button(self,text="B A C K",bg='black',fg='white',command=lambda:controller.show_frame(startpage))
        b5.place(bordermode=INSIDE,x=300,y=440,height=30,width=70)

        x=Label(self,text="Enter Your Book Id To Generate Your Ticket").place(x=50,y=260,height=20,width=320)
        ajk=StringVar()
        E=Entry(self,bg='#a6a6a6',textvariable=ajk)
        E.place(x=160,y=300,height=20,width=150)

        b1=Button(self,text="SUBMIT",bg='black',fg='white',command=lambda:go())
        b1.place(bordermode=INSIDE,x=170,y=350,height=30,width=70)


class promocode(tk.Frame):
     def __init__(self,parant,controller):
        tk.Frame.__init__(self,parant)

        self.config(background='white')
        render=ImageTk.PhotoImage(Image.open('promocode.png'))
        img=Label(self,image=render)
        img.image=render
        img.place(x=0,y=0)

        x=Label(self,bg="white",text="APPLY This Promo code!", font =('Comic Sans MS',20)).place(x=40,y=270,height=40,width=300)
        y=Label(self,bg="white",text="CINEMA100", font =('verdana',20)).place(x=50,y=340,height=40,width=300)
        z=Label(self,bg="white",text="(Applicable for 2 or more tickets)").place(x=45,y=380,height=30,width=300)

        b5=Button(self,text="B A C K",bg='black',fg='white',command=lambda:controller.show_frame(startpage))
        b5.place(bordermode=INSIDE,x=320,y=450,height=20,width=70)



class showtime(tk.Frame):
     def __init__(self,parant,controller):
        tk.Frame.__init__(self,parant)

        self.config(background='white')
        render=ImageTk.PhotoImage(Image.open('myticket1.jpg'))
        img=Label(self,image=render)
        img.image=render
        img.place(x=0,y=0)

        b5=Button(self,text="B A C K",bg='black',fg='white',command=lambda:controller.show_frame(startpage))
        b5.place(bordermode=INSIDE,x=300,y=440,height=30,width=70)

      
if __name__ == "__main__":
    global hell
    a=Application()
    a.mainloop()
def ada():
    a=Application()
    a.mainloop()
