import tkinter as tk
from tkinter import ttk
from tkinter import *
import AddVisitory
import Auth
import EnterDetails
from PIL import ImageTk
from PIL import Image

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self,"SIP 4rd Sem")
        tk.Tk.iconbitmap(self,default='./Assets/icon.ico')
        global root
        root=self
        container=tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.geometry('400x450')
        self.config(background='white')
        self.resizable(False,False)
        self.frames={}

        for F in (startpage,Login,Registration2):

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

        load=Image.open('./Assets/img1.png')
        render=ImageTk.PhotoImage(load)

        img=Label(self,image=render)
        img.image=render
        img.place(height=450,width=400)

        xx=Image.open('./Assets/login_img.jpg')
        login_img=ImageTk.PhotoImage(xx)
        xx=Image.open('./Assets/new_user_img.jpg')
        user=ImageTk.PhotoImage(xx)

        render=ImageTk.PhotoImage(Image.open('./Assets/hello.png'))
        img=Label(self,image=render)
        img.image=render
        img.place(x=180,y=360,height=53,width=40)

        butenter = Button(self,relief='flat',border=0,background='chartreuse3',image=login_img,command=lambda:controller.show_frame(Login))
        butenter.image=login_img
        butenter.place(bordermode=INSIDE,height=53,width=160,x=24,y=360)

        butquit = Button(self,image=user,relief='flat',border=0,command=lambda:controller.show_frame(Registration2))
        butquit.image=user
        butquit.place(bordermode=INSIDE,height=53,width=160,x=220,y=360)

class Login(tk.Frame):
    def __init__(self,parant,controller):
        tk.Frame.__init__(self, parant)
        self.config(background='#ffffff')
        titlelabel = tk.Label(self,fg='red',text='Login',bg='white', font='Verdana, 25')
        titlelabel.place(x=100,y=0,width=200)

        reglabel = tk.Label(self, text='Username',bg='white', font='Verdana, 12')
        reglabel.place(x=10,y=75,width=100,height=20)
        prelabel = tk.Label(self, text='Password',bg='white', font='Verdana, 12')
        prelabel.place(x=10,y=125,width=100,height=20)

        self.un= tk.Entry(self,textvariable=StringVar())
        self.un.place(x=130,y=75,width=125,height=20)
        self.pw = tk.Entry(self,show='*',textvariable=StringVar())
        self.pw.place(x=130,y=125,width=125,height=20)

        self.butsavedata = Button(self,background='white',activebackground='red', text='Submit', width=10,command=self.login)
        self.butsavedata.place(x=10,y=195,width=125,height=40)
        self.butquit = Button(self, text='Reset Fields',activebackground='red',background='white',width=10,command=self.reset)
        self.butquit.place(x=270,y=195,width=125,height=40)

        render=ImageTk.PhotoImage(Image.open('./Assets/back.png'))
        self.butquit1 = Button(self,background='white',relief='flat',image=render,activebackground='red',command=lambda:controller.show_frame(startpage))
        self.butquit1.place(x=00,y=0,width=100,height=50)
        self.butquit1.image=render
    def login(self):
        x=Auth.main(self.un.get(),self.pw.get())
        if x:
            global hell
            hell=x
            root.destroy()
        else:
            def retry():
                temp.destroy()
                self.reset()
            temp=Tk()
            Tk.iconbitmap(temp,"./Assets/error.ico")
            temp.geometry("250x200")
            temp.configure(background='white')
            temp.resizable(False,False)
            Tk.wm_title(temp,"Error")
            label=Label(temp,bg='white',fg='red',text="!!! Wrong Details!!!",font='Verdana, 20')
            label.place(x=0,y=0,width=250,height=50)
            a=Button(temp,background='white',relief='sunken',font='Verdana,20',text="Retry",command=retry)
            a.place(y=70,x=50,height=100,width=150)
            temp.mainloop()
    def reset(self):
        self.un.delete(0, 'end')
        self.pw.delete(0, 'end')


class Registration2(tk.Frame):
    def __init__(self,parant,controller):
        tk.Frame.__init__(self, parant)
        
        self.config(background='#ffffff')

        titlelabel = tk.Label(self,fg='red',text='Registration',bg='white', font='Verdana, 25')
        titlelabel.place(x=100,y=0,width=200)
        label1=tk.Label(self,bg='white',text="Name")
        label1.place(x=20,y=65,width=55)
        label6=tk.Label(self,fg='red',text='*',bg='white', font='Verdana,10')
        label6.place(x=75,y=115,width=7)
        label2=tk.Label(self,bg='white',text="Username")
        label2.place(x=20,y=115,width=55)
        label3=tk.Label(self,bg='white',text="Email")
        label3.place(x=20,y=165,width=55)
        label4=tk.Label(self,bg='white',text="Phone")
        label4.place(x=20,y=215,width=55)
        label5=tk.Label(self,bg='white',text="Password")
        label5.place(x=20,y=265,width=55)

        self.a1=tk.Entry(self,textvariable=StringVar())
        self.a1.place(x=100,y=65,width=155)
        self.a2=tk.Entry(self,textvariable=StringVar())
        self.a2.place(x=100,y=115,width=155)
        self.a3=tk.Entry(self,textvariable=StringVar())
        self.a3.place(x=100,y=165,width=155)
        self.a4=tk.Entry(self,textvariable=StringVar())
        self.a4.place(x=100,y=215,width=155)
        self.a5=tk.Entry(self,show="*",textvariable=StringVar())
        self.a5.place(x=100,y=265,width=155)

        button1=Button(self,background='white',activebackground='red', text='Submit', width=10,command=self.submit)
        button1.place(x=10,y=350,width=125,height=40)
        button2=Button(self,text="Reset Fields",background='white',activebackground='red',command=self.reset)
        button2.place(x=270,y=350,width=125,height=40)
        
        render=ImageTk.PhotoImage(Image.open('./Assets/back.png'))
        butquit1 = Button(self,background='white',relief='flat',image=render,activebackground='red',command=lambda:controller.show_frame(startpage))
        butquit1.place(x=0,y=0,width=100,height=50)
        butquit1.image=render


    def submit(self):
        reglist = [self.a1.get(),self.a2.get(),self.a3.get(),self.a4.get(),self.a5.get()]
        x=AddVisitory.addVisitor(reglist)
        if x:
            def retry():
                temp.destroy()
            temp=Tk()
            temp.config(background='#ffffff')
            temp.resizable(False,False)
            label=Label(temp,text="--> Registration Sucessfull <--",font='Verdana, 20',bg="white",fg='red').grid(column=0, row=1,padx=10, pady=30)
            a=Button(temp,text="Okay",command=retry,background='cyan',activebackground='red',font='Verdana,20').grid(column=0, row=2,padx=30, pady=10)
            temp.mainloop()
        else:
            def retry():
                temp.destroy()
                self.a2.delete(0, 'end')
            temp=Tk()
            temp.resizable(False,False)
            temp.config(background='#ffffff')
            label=Label(temp,text="!!Username already exists!!",font='Verdana, 20',bg="white",fg='red').grid(column=0, row=1,padx=10, pady=30)
            a=Button(temp,text="Retry",command=retry,background='cyan',activebackground='red',font='Verdana,20').grid(column=0, row=2,padx=30, pady=10)
            temp.mainloop()

    def reset(self):
        self.a1.delete(0, 'end')
        self.a2.delete(0, 'end')
        self.a3.delete(0, 'end')
        self.a4.delete(0, 'end')
        self.a5.delete(0, 'end')


my_gui = Application()
my_gui.mainloop()
try:
    if hell:
        EnterDetails.main()
except:
    quit()
