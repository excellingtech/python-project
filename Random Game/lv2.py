from tkinter import*
import pymysql
import random
top=Tk()
top.geometry('280x300')
top.config(bg='gray')
top.title('   :-)  Smile  ')
c=0
a=0

def reset():
   global c
   c=0
   def abc(num):
      global a
      a=num
      global c
      if (c<10):
         c=c+1
         r=random.randrange(1,11)
         if(a<r):
            m="small"
            var.set(m)
         elif(a>r):
            m="big"
            var.set(m)
         else:
            to=Tk()
            to.geometry('140x80')
            to.config(bg='gray')
            to.title('Choice')
            l=Message(to,text='You Are WINNER\n Congratulations',width=150).place(x=18,y=5)
            def go():
               top.destroy()
               to.destroy()
               import lv1
            def back():
               top.destroy()
               to.destroy()
            
            btn=Button(to,text='Play Again',command=go).place(x=20,y=50)
            btn=Button(to,text='Exit',command=back).place(x=90,y=50)
         a="The Random Number is ",r
         var1.set(a)
      else:
         top.destroy()
         import lv2n
            
   var=StringVar()
   var1=StringVar()
   lb=Label(text='☺   Play   with   your   Luck   ☺   ‰',bg='red',fg='yellow',height=2,width=40).place(x=0,y=0)
   msg=Message(text='NOTE:- Every time Random\n              Number will be Change !!',bg='gray',fg='yellow',width=180).place(x=3,y=40)
   btn=Button(text='Reset',command=reset,bd=4).place(x=220,y=45)
   en1=Entry(width=46,justify='center',textvariable=var,bg='gray',fg='yellow')
   en1.place(x=0,y=83)
   en2=Entry(width=46,justify='center',textvariable=var1,bg='gray',fg='yellow')
   en2.place(x=0,y=103)

   btn=Button(command=lambda:abc(1),text='1',width=3,bd=4).place(x=15,y=140)
   btn=Button(command=lambda:abc(2),text='2',width=3,bd=4).place(x=65,y=140)
   btn=Button(command=lambda:abc(3),text='3',width=3,bd=4).place(x=120,y=140)
   btn=Button(command=lambda:abc(4),text='4',width=3,bd=4).place(x=175,y=140)
   btn=Button(command=lambda:abc(5),text='5',width=3,bd=4).place(x=230,y=140)
   btn=Button(command=lambda:abc(6),text='6',width=3,bd=4).place(x=15,y=180)
   btn=Button(command=lambda:abc(7),text='7',width=3,bd=4).place(x=65,y=180)
   btn=Button(command=lambda:abc(8),text='8',width=3,bd=4).place(x=120,y=180)
   btn=Button(command=lambda:abc(9),text='9',width=3,bd=4).place(x=175,y=180)
   btn=Button(command=lambda:abc(10),text='10',width=3,bd=4).place(x=230,y=180)
   btn=Button(command=lambda:abc(11),text='11',width=3,bd=4).place(x=15,y=220)
   btn=Button(command=lambda:abc(12),text='12',width=3,bd=4).place(x=65,y=220)
   btn=Button(command=lambda:abc(13),text='13',width=3,bd=4).place(x=120,y=220)
   btn=Button(command=lambda:abc(14),text='14',width=3,bd=4).place(x=175,y=220)
   btn=Button(command=lambda:abc(15),text='15',width=3,bd=4).place(x=230,y=220)
   btn=Button(command=lambda:abc(16),text='16',width=3,bd=4).place(x=15,y=260)
   btn=Button(command=lambda:abc(17),text='17',width=3,bd=4).place(x=65,y=260)
   btn=Button(command=lambda:abc(18),text='18',width=3,bd=4).place(x=120,y=260)
   btn=Button(command=lambda:abc(19),text='19',width=3,bd=4).place(x=175,y=260)
   btn=Button(command=lambda:abc(20),text='20',width=3,bd=4).place(x=230,y=260)

   

reset()
top.mainloop()

