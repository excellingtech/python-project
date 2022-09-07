import tkinter
from tkinter import *
from tkinter import messagebox
import calendar
import random as r
from math import*
import calendar
import datetime
import random

var=tkinter.Tk()
var.title('Multi Task')
var.geometry('300x360')
var.config(background='gray')

def sum():
   a=int(ent1.get())
   b=int(ent2.get())
   c=a+b
   out.set(c)
def sub():
   a=int(ent1.get())
   b=int(ent2.get())
   c=a-b
   out.set(c)
def mul():
   a=int(ent1.get())
   b=int(ent2.get())
   c=a*b
   out.set(c)
def dev():
   a=int(ent1.get())
   b=int(ent2.get())
   c=a/b
   out.set(c)
   messagebox.showinfo('alert','Done')
   
out=StringVar()
lb1=tkinter.Label(text='First Value',background='red')
lb1.place(x=30,y=10)
ent1=tkinter.Entry(fg='red')
ent1.place(x=150,y=11)

lb2=tkinter.Label(text='Second Value',background='red')
lb2.place(x=30,y=50)
ent2=tkinter.Entry(fg='red')
ent2.place(x=150,y=51)

but=tkinter.Button(text='+',command=sum,background='yellow',fg='blue')
but.place(x=30,y=90)

but=tkinter.Button(text='-',command=sub,background='yellow',fg='blue')
but.place(x=60,y=90)

but=tkinter.Button(text='*',command=mul,background='yellow',fg='blue')
but.place(x=90,y=90)
but=tkinter.Button(text='/',command=dev,background='yellow',fg='blue')
but.place(x=120,y=90)

outp=tkinter.Entry(textvariable=out,fg='red')
outp.place(x=150,y=92)


#leap function
def leap():
   l=int(ent3.get())
   lp=calendar.isleap(l)
   if(lp==1):
      out1.set("YES")
   else:
      out1.set("No !!!")

out1=StringVar()
lb3=tkinter.Label(text='Leap Year',background='red')
lb3.place(x=30,y=150)
but=tkinter.Button(text='Is Leap ?',command=leap,background='yellow',fg='blue')
but.place(x=145,y=149)
ent3=tkinter.Entry(width="5",fg='red')
ent3.place(x=100,y=151)
ent4=tkinter.Entry(width="9",textvariable=out1,fg='red')
ent4.place(x=210,y=151)


#OTP function
def op():
    d='QWERTYUIOPLKJHGFDSAZXCVBNMmnbvcxzasdfghjklpoiuytrewq1234567890'
    l=len(d)
    v=""
    for i in range(4):
        v+=d[floor(r.random()*l)]
    o=repr(v)
    out2.set(o)
def otp():
    d='QWERTYUIOPLKJHGFDSAZXCVBNMmnbvcxzasdfghjklpoiuytrewq1234567890'
    l=len(d)
    v=""
    for i in range(6):
        v+=d[floor(r.random()*l)]
    o=repr(v)
    out2.set(o)

out2=StringVar()
lb4=tkinter.Label(text='Your OTP',background='red')
lb4.place(x=30,y=200)
but=tkinter.Button(text='4 Dg',command=op,background='yellow',fg='blue')
but.place(x=110,y=198)
but=tkinter.Button(text='6 Dg',command=otp,background='yellow',fg='blue')
but.place(x=150,y=198)
ent5=tkinter.Entry(width="10",textvariable=out2,fg='red')
ent5.place(x=205,y=200)


#WeekDay function
def findday():
   date=ent6.get()
   try:
      d=datetime.datetime.strptime(date,'%d %m %Y').weekday()
      r=calendar.day_name[d]
   except:
      r='Wrong Date'
   out3.set(r)

out3=StringVar()
lb5=tkinter.Label(text='Date -',background='red')
lb5.place(x=30,y=250)
ent6=tkinter.Entry(width='10',fg='red')
ent6.place(x=80,y=250)
but=tkinter.Button(text='Day',command=findday,background='yellow',fg='blue')
but.place(x=155,y=248)
ent7=tkinter.Entry(width='13',textvariable=out3,fg='red')
ent7.place(x=190,y=250)


#Random Game
def game():
   a=int(ent7.get())
   d=random.randrange(1,5)
   for i in range(0,5,1):
      if(a<=5):
         if (d==a):
            g='Winner'
            break
         else:
            g="Play again"
      else:
            g="Wrong Value"
            break
   out4.set(g)
   
out4=StringVar()
lb6=tkinter.Label(text='Random Num',background='red')
lb6.place(x=30,y=300)
ent7=tkinter.Entry(width='3',fg='red')
ent7.place(x=115,y=301)
but=tkinter.Button(text='Check',command=game,background='yellow',fg='blue')
but.place(x=144,y=298)
ent8=tkinter.Entry(width='13',textvariable=out4,fg='red')
ent8.place(x=190,y=301)



