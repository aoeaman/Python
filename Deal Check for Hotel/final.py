from tkinter import *
import tkinter as tk
def main(result):
    def submit():
        self.destroy()
    sol=result
    self=tk.Tk()
    self.config(background='white')
    self.resizable(False,False)
    tk.Label(self,text="Result",font='Times 20 bold',bg='white',fg='cyan').grid(row=0,column=0,padx=10, pady=20)
    if sol==1:
        tk.Label(self,text='User Can Book The Room',font='Times 20 bold',bg='white',fg='red').grid(row=1,column=0,padx=10, pady=10)
        bb=Button(self,text="Close",activebackground='red',command=submit,width=30,background='white')
        bb.grid(row=2,column=0,padx=10,pady=30)    
    else:
        tk.Label(self,text='User Will Not Book The Room',font='Times 20 bold',bg='white',fg='red').grid(row=1,column=0,padx=10, pady=10)
        bb=Button(self,text="Try Again",activebackground='red',background='white',command=submit,width=30)
        bb.grid(row=2,column=0,padx=30,pady=30)    

      
    self.mainloop()
