from tkinter import*
import random
top=Tk()
top.geometry('280x220')
top.config(bg='gray')
top.title('Level 1')
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
            l=Message(to,text='You Are WINNER\n    Go to Level 2',width=150).place(x=18,y=5)
            def go():
               top.destroy()
               to.destroy()
               import lv2
            def back():
               to.destroy()
               import lv1
            
            btn=Button(to,text='Go',command=go).place(x=30,y=50)
            btn=Button(to,text='Back',command=back).place(x=70,y=50)
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

   btn=Button(text='1',command=lambda:abc(1),width=3,bd=4).place(x=15,y=140)
   btn=Button(text='2',command=lambda:abc(2),width=3,bd=4).place(x=65,y=140)
   btn=Button(text='3',command=lambda:abc(3),width=3,bd=4).place(x=120,y=140)
   btn=Button(text='4',command=lambda:abc(4),width=3,bd=4).place(x=175,y=140)
   btn=Button(text='5',command=lambda:abc(5),width=3,bd=4).place(x=230,y=140)
   btn=Button(text='6',command=lambda:abc(6),width=3,bd=4).place(x=15,y=180)
   btn=Button(text='7',command=lambda:abc(7),width=3,bd=4).place(x=65,y=180)
   btn=Button(text='8',command=lambda:abc(8),width=3,bd=4).place(x=120,y=180)
   btn=Button(text='9',command=lambda:abc(9),width=3,bd=4).place(x=175,y=180)
   btn=Button(text='10',command=lambda:abc(10),width=3,bd=4).place(x=230,y=180)

   

reset()
top.mainloop()

