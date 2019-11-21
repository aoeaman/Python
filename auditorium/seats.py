from tkinter import *
import main
import details
import credientials

def lookup(q):
    master=Tk()
    master.geometry('400x450')
    master.config(background='#66a3ff')
    client=credientials.client
    db=client.test
    yy=db.M1S1.find_one({'id':q})
    current=yy['M1S1']
    def Submit():
        booked=[]
        check=[a1.get(),a2.get(),a3.get(),a4.get(),a5.get(),a6.get(),a7.get(),a8.get(),a9.get(),a10.get(),a11.get(),a12.get(),a13.get(),
               a14.get(),a15.get(),a16.get(),a17.get(),a18.get(),a19.get(),a20.get(),a21.get(),a22.get(),a23.get(),a24.get(),a25.get()]
        
        for i in range(0,25):
            if check[i]!=0 and current[i]!=check[i]:
                booked.append(i+1)
        
        qq=[len(booked),booked,yy['Time'],(yy['id']%10),len(booked*200),yy['Show'],yy,check]
        master.destroy()
        details.enter(qq)
    def Cancel():
        master.destroy()
        main.ada()
        


    a1 = IntVar(value=current[0])
    c1 = Checkbutton(master, text="1", variable=a1,bg='white',fg='red').place(x=10,y=20,width=50)

    a2 = IntVar(value=current[1])
    c2 = Checkbutton(master, text="2", variable=a2,bg='white',fg='red').place(x=70,y=20,width=50)

    a3 = IntVar(value=current[2])
    c3 = Checkbutton(master, text="3", variable=a3,bg='white',fg='red').place(x=210,y=20,width=50)

    a4 = IntVar(value=current[3])
    c4 = Checkbutton(master, text="4", variable=a4,bg='white',fg='red').place(x=270,y=20,width=50)

    a5 = IntVar(value=current[4])
    c5 = Checkbutton(master, text="5", variable=a5,bg='white',fg='red').place(x=330,y=20,width=50)

    a6 = IntVar(value=current[5])
    c6 = Checkbutton(master, text="6", variable=a6,bg='white',fg='red').place(x=10,y=60,width=50)

    a7 = IntVar(value=current[6])
    c7 = Checkbutton(master, text="7", variable=a7,bg='white',fg='red').place(x=70,y=60,width=50)

    a8 = IntVar(value=current[7])
    c8 = Checkbutton(master, text="8", variable=a8,bg='white',fg='red').place(x=210,y=60,width=50)

    a9 = IntVar(value=current[8])
    c9 = Checkbutton(master, text="9", variable=a9,bg='white',fg='red').place(x=270,y=60,width=50)

    a10 = IntVar(value=current[9])
    c10 = Checkbutton(master, text="10", variable=a10,bg='white',fg='red').place(x=330,y=60,width=50)

    a11 = IntVar(value=current[10])
    c11 = Checkbutton(master, text="11", variable=a11,bg='white',fg='red').place(x=10,y=100,width=50)

    a12 = IntVar(value=current[11])
    c12 = Checkbutton(master, text="12", variable=a12,bg='white',fg='red').place(x=70,y=100,width=50)

    a13 = IntVar(value=current[12])
    c13 = Checkbutton(master, text="13", variable=a13,bg='white',fg='red').place(x=210,y=100,width=50)

    a14 = IntVar(value=current[13])
    c14 = Checkbutton(master, text="14", variable=a14,bg='white',fg='red').place(x=270,y=100,width=50)

    a15 = IntVar(value=current[14])
    c15 = Checkbutton(master, text="15", variable=a15,bg='white',fg='red').place(x=330,y=100,width=50)

    a16 = IntVar(value=current[15])
    c16 = Checkbutton(master, text="16", variable=a16,bg='white',fg='red').place(x=10,y=140,width=50)

    a17 = IntVar(value=current[16])
    c17 = Checkbutton(master, text="17", variable=a17,bg='white',fg='red').place(x=70,y=140,width=50)

    a18 = IntVar(value=current[17])
    c18 = Checkbutton(master, text="18", variable=a18,bg='white',fg='red').place(x=210,y=140,width=50)

    a19 = IntVar(value=current[18])
    c19 = Checkbutton(master, text="19", variable=a19,bg='white',fg='red').place(x=270,y=140,width=50)

    a20 = IntVar(value=current[19])
    c20 = Checkbutton(master, text="20", variable=a20,bg='white',fg='red').place(x=330,y=140,width=50)

    a21 = IntVar(value=current[20])
    c21 = Checkbutton(master, text="21", variable=a21,bg='white',fg='red').place(x=10,y=180,width=50)

    a22 = IntVar(value=current[21])
    c22 = Checkbutton(master, text="22", variable=a22,bg='white',fg='red').place(x=70,y=180,width=50)

    a23 = IntVar(value=current[22])
    c23= Checkbutton(master, text="23", variable=a23,bg='white',fg='red').place(x=210,y=180,width=50)

    a24 = IntVar(value=current[23])
    c24 = Checkbutton(master, text="24", variable=a24,bg='white',fg='red').place(x=270,y=180,width=50)

    a25 = IntVar(value=current[24])
    c25 = Checkbutton(master, text="25", variable=a25,bg='white',fg='red').place(x=330,y=180,width=50)


    if a1.get()==1:
        c1 = Checkbutton(master, text="1", variable=a1,bg='white',fg='red',state='disabled').place(x=10,y=20,width=50)

    if a2.get()==1:
        c2 = Checkbutton(master, text="2", variable=a2,bg='white',fg='red',state='disabled').place(x=70,y=20,width=50)

    if a3.get()==1:
        c3 = Checkbutton(master, text="3", variable=a3,bg='white',fg='red',state='disabled').place(x=210,y=20,width=50)

    if a4.get()==1:
        c4 = Checkbutton(master, text="4", variable=a4,bg='white',fg='red',state='disabled').place(x=270,y=20,width=50)

    if a5.get()==1:
        c5 = Checkbutton(master, text="5", variable=a5,bg='white',fg='red',state='disabled').place(x=330,y=20,width=50)

    if a6.get()==1:
        c6 = Checkbutton(master, text="6", variable=a6,bg='white',fg='red',state='disabled').place(x=10,y=60,width=50)

    if a7.get()==1:
        c7 = Checkbutton(master, text="7", variable=a7,bg='white',fg='red',state='disabled').place(x=70,y=60,width=50)

    if a8.get()==1:
        c8 = Checkbutton(master, text="8", variable=a8,bg='white',fg='red',state='disabled').place(x=210,y=60,width=50)

    if a9.get()==1:
        c9 = Checkbutton(master, text="9", variable=a9,bg='white',fg='red',state='disabled').place(x=270,y=60,width=50)

    if a10.get()==1:
        c10 = Checkbutton(master, text="10", variable=a10,bg='white',fg='red',state='disabled').place(x=330,y=60,width=50)

    if a11.get()==1:
        c11 = Checkbutton(master, text="11", variable=a11,bg='white',fg='red',state='disabled').place(x=10,y=100,width=50)

    if a12.get()==1:
        c12 = Checkbutton(master, text="12", variable=a12,bg='white',fg='red',state='disabled').place(x=70,y=100,width=50)

    if a13.get()==1:
        c13 = Checkbutton(master, text="13", variable=a13,bg='white',fg='red',state='disabled').place(x=210,y=100,width=50)

    if a14.get()==1:
        c14 = Checkbutton(master, text="14", variable=a14,bg='white',fg='red',state='disabled').place(x=270,y=100,width=50)

    if a15.get()==1:
        c15 = Checkbutton(master, text="15", variable=a15,bg='white',fg='red',state='disabled').place(x=330,y=100,width=50)

    if a16.get()==1:
        c16 = Checkbutton(master, text="16", variable=a16,bg='white',fg='red',state='disabled').place(x=10,y=140,width=50)

    if a17.get()==1:
        c17 = Checkbutton(master, text="17", variable=a17,bg='white',fg='red',state='disabled').place(x=70,y=140,width=50)

    if a18.get()==1:
        c18 = Checkbutton(master, text="18", variable=a18,bg='white',fg='red',state='disabled').place(x=210,y=140,width=50)

    if a19.get()==1:
        c19 = Checkbutton(master, text="19", variable=a19,bg='white',fg='red',state='disabled').place(x=270,y=140,width=50)

    if a20.get()==1:
        c20 = Checkbutton(master, text="20", variable=a20,bg='white',fg='red',state='disabled').place(x=330,y=140,width=50)

    if a21.get()==1:
        c21 = Checkbutton(master, text="21", variable=a21,bg='white',fg='red',state='disabled').place(x=10,y=180,width=50)

    if a22.get()==1:
        c22 = Checkbutton(master, text="22", variable=a22,bg='white',fg='red',state='disabled').place(x=70,y=180,width=50)

    if a23.get()==1:
        c23= Checkbutton(master, text="23", variable=a23,bg='white',fg='red',state='disabled').place(x=210,y=180,width=50)

    if a24.get()==1:
        c24 = Checkbutton(master, text="24", variable=a24,bg='white',fg='red',state='disabled').place(x=270,y=180,width=50)

    if a25.get()==1:
        c25 = Checkbutton(master, text="25", variable=a25,bg='white',fg='red',state='disabled').place(x=330,y=180,width=50)


        

    x=Label(master,text="All Eyes This Way Please",bg='white').place(x=60,y=280,height=15,width=280)
    
    SubmitButton=Button(master,text='submit',font='verdana 16',bg='white',relief='flat',border=5,command=Submit).place(x=50,y=380,height=40,width=100)



    HomeButton=Button(master,text='Cancel',command=Cancel,font='verdana 16',bg='white',relief='flat',border=5).place(x=250,y=380,height=40,width=100)


    master.mainloop()

