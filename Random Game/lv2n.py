from tkinter import*
import pymysql
import random
top=Tk()
top.geometry('60x110')
top.config(bg='gray')
top.title('   :-)  Smile  ')

def yes():
   top.destroy()
   import lv1
def ex():
   top.destroy()

l=Message(text='GAME OVER ! \n\nYou have one more chance').place(x=18,y=5)
btn=Button(text='PLAY',command=yes).place(x=23,y=80)
btn=Button(text='Exit',command=ex).place(x=68,y=80)
top.mainloop()
