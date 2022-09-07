import tkinter as tk
from tkinter import *
var=tk.Tk()
var.title('Converter')
var.geometry('300x260')
var.config(bg='gray')

def bitcoin():
   a=int(en.get())
   b=a*798942
   out.set(b)
def mb():
   a=int(en3.get())
   b=a*1024
   out1.set(b)
def petrol():
   a=int(en4.get())
   b=round((a/70.41),2)
   out2.set(b)
   
out=StringVar()
out1=StringVar()
out2=StringVar()
lb=tk.Label(text='Bitcoin to Rupees',height='2',width='15',bg='red')
lb.place(x=90,y=10)
en=tk.Entry(width='5',fg='blue')
en.place(x=30,y=52)
lb1=tk.Label(text='BitCoin',bg='yellow')
lb1.place(x=70,y=50)
btn=tk.Button(text='>>',command=bitcoin)
btn.place(x=120,y=50)
en2=tk.Entry(textvariable=out,width='10',fg='blue')
en2.place(x=150,y=52)
lb2=tk.Label(text='Rupees',bg='yellow')
lb2.place(x=220,y=51)

lb3=tk.Label(text="mb's  to  Kb's",height='2',width='15',bg='red')
lb3.place(x=90,y=90)
en3=tk.Entry(width='5',fg='blue')
en3.place(x=50,y=134)
lb4=tk.Label(text='MB',bg='yellow')
lb4.place(x=90,y=133)
btn=tk.Button(text='>>',command=mb)
btn.place(x=120,y=132)
en4=tk.Entry(width='10',textvariable=out1,fg='blue')
en4.place(x=150,y=134)
lb5=tk.Label(text='KB',bg='yellow')
lb5.place(x=220,y=132)

lb=tk.Label(text='Petrol Rate calculater',height='2',width='20',bg='red')
lb.place(x=70,y=170)
en4=tk.Entry(width='5')
en4.place(x=30,y=214)
lb1=tk.Label(text='Rupees',bg='yellow')
lb1.place(x=70,y=212)
btn=tk.Button(text='>>',command=petrol)
btn.place(x=120,y=210)
en5=tk.Entry(textvariable=out2,width='8')
en5.place(x=150,y=212)
lb1=tk.Label(text='Letter',bg='yellow')
lb1.place(x=210,y=212)

var.mainloop()
