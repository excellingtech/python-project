import tkinter as tk
import inflect
from tkinter import *
var=tk.Tk()
var.title('Sample')
var.geometry('270x130')
var.config(bg='gray')


#def main():
def convert():
   a=int(en.get())
   e=inflect.engine()
   out.set((e.number_to_words(a)).capitalize())
def close():
   var.destroy()

out=StringVar()
lb=Label(text='< ***** Number to Words ***** >',height='2',width='25',fg='red')
lb.place(x=50,y=10)
en=Entry(width='10',justify='center')
en.place(x=30,y=62)
but=Button(text='Change',command=convert,bg='yellow').place(x=105,y=58)
   #reset=Button(text = "Reset", command =main,bg='red').place(x=170,y=58)
quit=Button(text="Quit",command = close,bg='red').place(x=220,y=58)
en2=Entry(width='45',textvariable=out,justify='center').place(x=0,y=90)
var.mainloop()
#main()
