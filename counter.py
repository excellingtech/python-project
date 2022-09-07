import tkinter as tk
from tkinter import *

v=tk.Tk()
v.geometry('200x280')
v.title('Counter')
v.config(background='gray')
#n=0

def twoth():
   #global n
   a=int(en.get())
   #n=a%2000
   b=a//2000
   out.set(b)
def panso():
   a=int(en.get())
   b=a//500
   out.set(b)
def doso():
   a=int(en.get())
   b=a//200
   out.set(b)
def so():
   a=int(en.get())
   b=a//100
   out.set(b)
def pcas():
   a=int(en.get())
   b=a//50
   out.set(b)
def besh():
   a=int(en.get())
   b=a//20
   out.set(b)
def das():
   a=int(en.get())
   b=a//10
   out.set(b)
def pach():
   a=int(en.get())
   b=a//5
   out.set(b)
def do():
   a=int(en.get())
   b=a//2
   out.set(b)
def ak():
   a=int(en.get())
   b=a//1
   out.set(b)

def list():
   a=int(en.get())
   z=a//2000
   a=a%2000
   out1.set(('2000= ',z))
   d=a//500
   a=a%500
   out2.set(('500 = ',d))
   e=a//200
   a=a%200
   out3.set(('200 = ',e))
   f=a//100
   a=a%100
   out4.set(('100 = ',f))
   x=a//50
   a=a%50
   out5.set(('50  = ',x))
   c=a//20
   a=a%20
   out6.set(('20  = ',c))
   g=a//10
   a=a%10
   out7.set(('10  = ',g))
   h=a//5
   a=a%5
   out8.set(('5  = ',h))
   i=a//2
   a=a%2
   out9.set(('2  = ',i))
   j=a//1
   a=a%1
   out10.set(('1  = ',j))
   
   
out=StringVar()
out1=StringVar()
out2=StringVar()
out3=StringVar()
out4=StringVar()
out5=StringVar()
out6=StringVar()
out7=StringVar()
out8=StringVar()
out9=StringVar()
out10=StringVar()
lb=tk.Label(text='Amount',fg='red')
lb.place(x=20,y=20)
en=tk.Entry(width='10',fg='blue')
en.place(x=80,y=20)
otp=tk.Entry(textvariable=out,width='3',fg='blue')
otp.place(x=160,y=20)
btn=tk.Button(text='2000',command=twoth,background='yellow')
btn.place(x=24,y=45)
btn=tk.Button(text='500',command=panso,background='yellow')
btn.place(x=70,y=45)
btn=tk.Button(text='200',command=doso,background='yellow')
btn.place(x=110,y=45)
btn=tk.Button(text='100',command=so,background='yellow')
btn.place(x=150,y=45)
btn=tk.Button(text='50',command=pcas,background='yellow')
btn.place(x=25,y=80)
btn=tk.Button(text='20',command=besh,background='yellow')
btn.place(x=55,y=80)
btn=tk.Button(text='10',command=das,background='yellow')
btn.place(x=85,y=80)
btn=tk.Button(text='5',command=pach,background='yellow')
btn.place(x=115,y=80)
btn=tk.Button(text='2',command=do,background='yellow')
btn.place(x=136,y=80)
btn=tk.Button(text='1',command=ak,background='yellow')
btn.place(x=160,y=80)

btn=tk.Button(text='List',width='15',background='red',command=list)
btn.place(x=42,y=110)
en1=tk.Entry(width='10',fg='blue',textvariable=out1)
en1.place(x=30,y=140)
en2=tk.Entry(width='10',fg='blue',textvariable=out2)
en2.place(x=30,y=160)
en3=tk.Entry(width='10',fg='blue',textvariable=out3)
en3.place(x=30,y=180)
en4=tk.Entry(width='10',fg='blue',textvariable=out4)
en4.place(x=30,y=200)
en5=tk.Entry(width='10',fg='blue',textvariable=out5)
en5.place(x=30,y=220)
en6=tk.Entry(width='10',fg='blue',textvariable=out6)
en6.place(x=100,y=140)
en7=tk.Entry(width='10',fg='blue',textvariable=out7)
en7.place(x=100,y=160)
en8=tk.Entry(width='10',fg='blue',textvariable=out8)
en8.place(x=100,y=180)
en9=tk.Entry(width='10',fg='blue',textvariable=out9)
en9.place(x=100,y=200)
en10=tk.Entry(width='10',fg='blue',textvariable=out10)
en10.place(x=100,y=220)

lb=tk.Label(text='Amount Calculater',bg='red',fg='yellow',width='28',height='2')
lb.place(x=0,y=250)

v.mainloop()
