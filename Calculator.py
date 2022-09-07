from tkinter import*
cal=Tk()
cal.geometry("360x400")
cal.title("CALCULATOR")
calabel=Label(cal,text="CALCULATOR",fg='blue',bg="yellow",font=("algerian",30,'bold'))
calabel.pack(side=TOP)
cal.config(background="purple")
cal.resizable(width=False,height=False)

textin=StringVar()
operator=""

def clickbut(number):
    #lambda:clickbut(1)
    global operator
    operator=operator+str(number)
    textin.set(operator)

def equlbut():
    global operator
    sumup=str(eval(operator))
    textin.set(sumup)
    operator=''

def clrbut():
    global operator
    operator=''
    textin.set("")

caltext=Entry(cal,font=("Courier New",12,'bold'),textvar=textin,width=25,bd=5,bg='lime')
caltext.pack()

but1=Button(cal,padx=14,pady=14,bd=4,bg='pink',command=lambda:clickbut(1),text='1',font=("Courier New",16,'bold'))
but1.place(x=10,y=100)

but2=Button(cal,padx=14,pady=14,bd=4,bg='pink',command=lambda:clickbut(2),text='2',font=("Courier New",16,'bold'))
but2.place(x=10,y=170)

but3=Button(cal,padx=14,pady=14,bd=4,bg='pink',command=lambda:clickbut(3),text='3',font=("Courier New",16,'bold'))
but3.place(x=10,y=240)

but4=Button(cal,padx=14,pady=14,bd=4,bg='pink',command=lambda:clickbut(4),text='4',font=("Courier New",16,'bold'))
but4.place(x=75,y=100)

but5=Button(cal,padx=14,pady=14,bd=4,bg='pink',command=lambda:clickbut(5),text='5',font=("Courier New",16,'bold'))
but5.place(x=75,y=170)

but6=Button(cal,padx=14,pady=14,bd=4,bg='pink',command=lambda:clickbut(6),text='6',font=("Courier New",16,'bold'))
but6.place(x=75,y=240)

but7=Button(cal,padx=14,pady=14,bd=4,bg='pink',command=lambda:clickbut(7),text='7',font=("Courier New",16,'bold'))
but7.place(x=140,y=100)

but8=Button(cal,padx=14,pady=14,bd=4,bg='pink',command=lambda:clickbut(8),text='8',font=("Courier New",16,'bold'))
but8.place(x=140,y=170)

but9=Button(cal,padx=14,pady=14,bd=4,bg='pink',command=lambda:clickbut(9),text='9',font=("Courier New",16,'bold'))
but9.place(x=140,y=240)

but0=Button(cal,padx=14,pady=14,bd=4,bg='pink',command=lambda:clickbut(0),text='0',font=("Courier New",16,'bold'))
but0.place(x=10,y=310)

but00=Button(cal,padx=7,pady=14,bd=4,bg='pink',command=lambda:clickbut("00"),text='00',font=("Courier New",16,'bold'))
but00.place(x=75,y=310)

butdot=Button(cal,padx=14,pady=14,bd=4,bg='pink',command=lambda:clickbut("."),text='.',font=("Courier New",16,'bold'))
butdot.place(x=140,y=310)

butpl=Button(cal,padx=14,pady=14,bd=4,bg='powder blue',command=lambda:clickbut("+"),text='+',font=("Courier New",16,'bold'))
butpl.place(x=205,y=100)

butsub=Button(cal,padx=14,pady=14,bd=4,bg='powder blue',command=lambda:clickbut("-"),text='-',font=("Courier New",16,'bold'))
butsub.place(x=205,y=170)

butml=Button(cal,padx=14,pady=14,bd=4,bg='powder blue',command=lambda:clickbut("*"),text='*',font=("Courier New",16,'bold'))
butml.place(x=205,y=240)

butdiv=Button(cal,padx=14,pady=14,bd=4,bg='powder blue',command=lambda:clickbut("/"),text='/',font=("Courier New",16,'bold'))
butdiv.place(x=205,y=310)

butclear=Button(cal,padx=20,pady=49,bd=4,bg='red',command=clrbut,text='C',font=("Courier New",16,'bold'))
butclear.place(x=270,y=100)

butequal=Button(cal,padx=20,pady=49,bd=4,bg='green',command=equlbut,text='=',font=("Courier New",16,'bold'))
butequal.place(x=270,y=240)

cal.mainloop()
