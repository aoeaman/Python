import tkinter as tkk
from tkinter import *
import tkinter as tk
import knn
import final

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self,"Hotel Details")
        container=tk.Frame(self)
        self.geometry("500x600")
        global root
        root=self
        self.resizable(False,False)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.frames={}
        

        frame=StartPage(container,self)
        self.frames[StartPage]=frame
        frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(StartPage)
        
    def show_frame(self,cont):
        frame=self.frames[cont]
        frame.tkraise()
        
class StartPage(tk.Frame):
    def __init__(self,parant,controller):
        tk.Frame.__init__(self, parant)
        self.config(background='#ffffff')
        tk.Label(self,text="Booking Form",font='Times 30 bold',bg='white',fg="red").place(x=100,y=20,width=300)
        
        
        tk.Label(self,text='WiFi',bg='white', font='Verdana, 12').place(x=0,y=100,width=150)
        self.w=IntVar()
        self.w.set(1)
        Radiobutton(self, text="Yes", variable=self.w, value=1,bg='white').place(x=150,y=100,width=150)
        Radiobutton(self, text="No", variable=self.w, value=0,bg='white').place(x=300,y=100,width=150)
        
        
        tk.Label(self,text='Breakfast',bg='white', font='Verdana, 12').place(x=0,y=150,width=150)
        self.b=IntVar()
        self.b.set(1)
        Radiobutton(self, text="Yes", variable=self.b, value=1,bg='white').place(x=150,y=150,width=150)
        Radiobutton(self, text="No", variable=self.b, value=0,bg='white').place(x=300,y=150,width=150)
    
        
        tk.Label(self,text='AC',bg='white', font='Verdana, 12').place(x=0,y=200,width=150)
        self.a=IntVar()
        self.a.set(1)
        Radiobutton(self, text="Yes", variable=self.a,bg='white', value=1).place(x=150,y=200,width=150)
        Radiobutton(self, text="No", variable=self.a,bg='white', value=0).place(x=300,y=200,width=150)
        
        tk.Label(self,text='No of Persons',bg='white', font='Verdana, 12').place(x=0,y=250,width=150)
        self.Persons=IntVar()
        self.Persons.set(1)
        Choices={1,2,3,4,5}
        self.popupMenu=OptionMenu(self,self.Persons,*Choices)
        self.popupMenu.config(bg='white', font='Verdana, 12')
        self.popupMenu.place(x=150,y=250,width=150)
        
        
        tk.Label(self,text='Hotel Star',bg='white', font='Verdana, 12').place(x=0,y=300,width=150)
        self.star=IntVar()
        self.star.set(1)
        self.popupMenu=OptionMenu(self,self.star,*Choices)
        self.popupMenu.config(bg='white', font='Verdana, 12')
        self.popupMenu.place(x=150,y=300,width=150)
        
        
        tk.Label(self,text='Days Of Booking',bg='white', font='Verdana, 12').place(x=0,y=350,width=150)
        self.days=IntVar()
        self.days.set(1)
        self.popupMenu=OptionMenu(self,self.days,*Choices)
        self.popupMenu.config(bg='white', font='Verdana, 12')
        self.popupMenu.place(x=150,y=350,width=150)
        
        
        tk.Label(self,text="Season",bg='white', font='Verdana, 12').place(x=0,y=400,width=150)
        self.season=IntVar()
        self.season.set(1)
        tkk.Radiobutton(self,text="Low",value=1,variable=self.season,bg='white', font='Verdana, 12').place(x=150,y=400,width=120)
        tkk.Radiobutton(self,text="Medium",value=2,variable=self.season,bg='white', font='Verdana, 12').place(x=270,y=400,width=120)
        tkk.Radiobutton(self,text="High",value=3,variable=self.season,bg='white', font='Verdana, 12').place(x=390,y=400,width=120)
        
        
        tk.Label(self,text="Price",bg='white', font='Verdana, 12').place(x=0,y=450,width=150)
        self.Price=IntVar()
        self.Price.set(1000)
        pp=[1000 ,2000 ,3000 ,4000 ,5000 ,6000]
        self.popupMenu=OptionMenu(self,self.Price,*pp)
        self.popupMenu.config(width=1,bg='white', font='Verdana, 12')
        self.popupMenu.place(x=150,y=450,width=150)
        
        bb=Button(self,text="Submit",background='white',activebackground='red',command=self.Submit,width=10,font='Verdana, 12')
        bb.place(x=75,y=525,height=50,width=150)
        bb1=Button(self,text="Close",background='white',activebackground='red',command=root.destroy,width=10,font='Verdana, 12')
        bb1.place(x=275,y=525,height=50,width=150)

    def Submit(self):
        
            fuk_u=[self.a.get(),self.b.get(),self.days.get(), self.star.get(),
                   self.Persons.get(),self.Price.get(),self.season.get(),self.w.get()] 
            www=knn.knn(fuk_u)
            wwww=final.main(www)
                   
                   
def main():
    aa=Application()
    aa.mainloop()
