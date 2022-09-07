from tkinter import*
import math
#import parser,tkinter.messagebox

r=Tk()
r.title("Scientific Calculator")
#r.config(background='purple')
r.resizable(width=False,height=False)
r.geometry('960x590')

calc=Frame(r)
calc.grid()

class Calc():
    def __init__(self):
        self.total=0
        self.current=""
        self.input_value=True
        self.check_sum=False
        self.op=""
        self.result=False

    def numberEnter(self,num):
        self.result=False
        firstsum=txtDisplay.get()
        secondsum=str(num)
        if self.input_value:
            self.current=secondsum
            self.input_value=False
        else:
            if secondsum=='.':
                if secondsum in firstsum:
                    return
            self.current=firstsum+secondsum
        self.display(self.current)

    def sum_of_total(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum==True:
            self.valid_function()
        else:
            self.total=float(txtDisplay.get())
            
    def display(self,value):
        txtDisplay.delete(0,END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        if self.op=='add':
            self.total+=self.current
        if self.op=='sub':
            self.total-=self.current
        if self.op=='muti':
            self.total*=self.current
        if self.op=='divide':
            self.total/=self.current
        if self.op=='mod':
            self.total%=self.current
        self.input_value=True
        self.check_sum=False
        self.display(self.total)

    def operation(self,op):
        self.current=float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total=self.current
            self.input_value=True
        self.check_sum=True
        self.op=op
        self.result=False

    def Clear_Entry(self):
        self.result=False
        self.current='0'
        self.display(0)
        self.input_value=True

    def all_Clear_Entry(self):
        self.Clear_Entry()
        self.total=0

    def mathPM(self):
        self.result=False
        self.current=-(float(txtDisplay.get()))
        self.display(self.current)

    def sqrt(self):
        self.result=False
        self.current=math.sqrt (float(txtDisplay.get()))
        self.display(self.current)

    def cos(self):
        self.result=False
        self.current=math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cosh(self):
        self.result=False
        self.current=math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        
    def tan(self):
        self.result=False
        self.current=math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)                      

    def tanh(self):
        self.result=False
        self.current=math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        
    def sin(self):
        self.result=False
        self.current=math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sinh(self):
        self.result=False
        self.current=math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def log(self):
        self.result=False
        self.current=math.log(float(txtDisplay.get()))
        self.display(self.current)

    def exp(self):
        self.result=False
        self.current=math.exp(float(txtDisplay.get()))
        self.display(self.current)

    def mod(self):
        self.result=False
        self.current=math.mod(float(txtDisplay.get()))
        self.display(self.current)
        
    def pi(self):
        self.result=False
        self.current=math.pi
        self.display(self.current)

    def tau(self):
        self.result=False
        self.current=math.tau
        self.display(self.current)

    def e(self):
        self.result=False
        self.current=math.e
        self.display(self.current)

    def atanh(self):
        self.result=False
        self.current=math.atanh(float(txtDisplay.get()))
        self.display(self.current)

    def acosh(self):
        self.result=False
        self.current=math.acosh(float(txtDisplay.get()))
        self.display(self.current)

    def asinh(self):
        self.result=False
        self.current=math.asinh(float(txtDisplay.get()))
        self.display(self.current)

    def degrees(self):
        self.result=False
        self.current=math.degrees(float(txtDisplay.get()))
        self.display(self.current)

    def log2(self):
        self.result=False
        self.current=math.log2(float(txtDisplay.get()))
        self.display(self.current)

    def log10(self):
        self.result=False
        self.current=math.log10(float(txtDisplay.get()))
        self.display(self.current)

    def fact(self):
        self.result=False
        self.current=math.factorial(float(txtDisplay.get()))
        self.display(self.current)

    def power(self):
        self.result=False
        self.current=math.pow(float(txtDisplay.get()))
        self.display(self.current)

added_value=Calc()

txtDisplay=Entry(calc,font=('arial',20,'bold'),bg='lime',bd=30,width=28,justify=RIGHT)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,'0')

numberpad='789456123'
i=0
btn=[]
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc,width=6,height=2,font=('arial',20,'bold'),bg='pink',bd=4,text=numberpad[i]))
        btn[i].grid(row=j,column=k,pady=1)
        btn[i]['command']=lambda x= numberpad[i]:added_value.numberEnter(x)
        i+=1
#=============================================#===========================================#=======================================
btnClear=Button(calc,text='C',width=6,height=2,font=('arial',20,'bold'),bd=4,bg='orange',command=added_value.Clear_Entry).grid(row=1,column=0,pady=1)
btnAllClear=Button(calc,text='AC',width=6,height=2,font=('arial',20,'bold'),bd=4,bg='red',command=added_value.all_Clear_Entry).grid(row=1,column=1,pady=1)
btnsq=Button(calc,text='Sqrt',width=6,height=2,font=('arial',20,'bold'),bd=4,bg='skyblue',command=added_value.sqrt).grid(row=1,column=2,pady=1)
btnAdd=Button(calc,text='+',width=6,height=2,font=('arial',20,'bold'),bd=4,bg='skyblue',command=lambda:added_value.operation('add')).grid(row=1,column=3,pady=1)
btnSub=Button(calc,text='-',width=6,height=2,font=('arial',20,'bold'),bd=4,bg='skyblue',command=lambda:added_value.operation('sub')).grid(row=2,column=3,pady=1)
btnMul=Button(calc,text='*',width=6,height=2,font=('arial',20,'bold'),bd=4,bg='skyblue',command=lambda:added_value.operation('muti')).grid(row=3,column=3,pady=1)
btnDiv=Button(calc,text='/',width=6,height=2,font=('arial',20,'bold'),bd=4,bg='skyblue',command=lambda:added_value.operation('divide')).grid(row=4,column=3,pady=1)
btnZero=Button(calc,text='0',width=6,height=2,font=('arial',20,'bold'),bd=4,bg='skyblue',command=lambda:added_value.numberEnter(0)).grid(row=5,column=0,pady=1)
btnDot=Button(calc,text='.',width=6,height=2,font=('arial',20,'bold'),bd=4,bg='skyblue',command=lambda:added_value.numberEnter('.')).grid(row=5,column=1,pady=1)
btnPM=Button(calc,text=chr(177),width=6,height=2,font=('arial',20,'bold'),bd=4,bg='skyblue',command=added_value.mathPM).grid(row=5,column=2,pady=1)
btnEqual=Button(calc,text='=',width=6,height=2,font=('arial',20,'bold'),bd=4,bg='green',command=added_value.sum_of_total).grid(row=5,column=3,pady=1)
#========================================================Scientific Calculator==========================================================
btnPi=Button(calc,text='Pi',width=6,height=2,font=('arial',20,'bold'),bd=4,bg='powder blue',command=added_value.pi).grid(row=1,column=4,pady=1)
btnSin=Button(calc,text='Sin',width=6,height=2,font=('arial',20,'bold'),bd=4,bg='powder blue',command=added_value.sin).grid(row=1,column=5,pady=1)
btnCos=Button(calc,text='Cos',width=6,height=2,font=('arial',20,'bold'),bd=4,bg='powder blue',command=added_value.cos).grid(row=1,column=6,pady=1)
btnTan=Button(calc,text='Tan',width=6,height=2,font=('arial',20,'bold'),bd=4,bg='powder blue',command=added_value.tan).grid(row=1,column=7,pady=1)
#===================================================================================================================================
btn2Pi=Button(calc,text='2Pi',width=6,height=2,font=('arial',20,'bold'),bd=4,bg='powder blue',command=added_value.tau).grid(row=2,column=4,pady=1)
btnSinh=Button(calc,text='Sinh',width=6,height=2,font=('arial',20,'bold'),bd=4,bg='powder blue',command=added_value.sinh).grid(row=2,column=5,pady=1)
btnCosh=Button(calc,text='Cosh',width=6,height=2,font=('arial',20,'bold'),bd=4,bg='powder blue',command=added_value.cosh).grid(row=2,column=6,pady=1)
btnTanh=Button(calc,text='Tanh',width=6,height=2,font=('arial',20,'bold'),bd=4,bg='powder blue',command=added_value.tanh).grid(row=2,column=7,pady=1)
#====================================================================================================================================
btnlog=Button(calc,text='log',width=6,height=2,font=('arial',20,'bold'),bd=4,bg='powder blue',command=added_value.log).grid(row=3,column=4,pady=1)
btnExp=Button(calc,text='Exp',width=6,height=2,font=('arial',20,'bold'),bd=4,bg='powder blue',command=added_value.exp).grid(row=3,column=5,pady=1)
btnMod=Button(calc,text='Mod',width=6,height=2,font=('arial',20,'bold'),bd=4,bg='powder blue',command=added_value.mod).grid(row=3,column=6,pady=1)
btnE=Button(calc,text='e',width=6,height=2,font=('arial',20,'bold'),bd=4,bg='powder blue',command=added_value.e).grid(row=3,column=7,pady=1)
#===================================================================================================================================
btnlog2=Button(calc,text='log2',width=6,height=2,font=('arial',20,'bold'),bd=4,bg='powder blue',command=added_value.log2).grid(row=4,column=4,pady=1)
btnaSinh=Button(calc,text='asinh',width=6,height=2,font=('arial',20,'bold'),bd=4,bg='powder blue',command=added_value.asinh).grid(row=4,column=5,pady=1)
btnaCosh=Button(calc,text='acosh',width=6,height=2,font=('arial',20,'bold'),bd=4,bg='powder blue',command=added_value.acosh).grid(row=4,column=6,pady=1)
btnaTanh=Button(calc,text='atanh',width=6,height=2,font=('arial',20,'bold'),bd=4,bg='powder blue',command=added_value.atanh).grid(row=4,column=7,pady=1)
#====================================================================================================================================
btnlog10=Button(calc,text='log10',width=6,height=2,font=('arial',20,'bold'),bd=4,bg='powder blue',command=added_value.log10).grid(row=5,column=4,pady=1)
btnFact=Button(calc,text='fact',width=6,height=2,font=('arial',20,'bold'),bd=4,bg='powder blue',command=added_value.fact).grid(row=5,column=5,pady=1)
btnDeg=Button(calc,text='Deg',width=6,height=2,font=('arial',20,'bold'),bd=4,bg='powder blue',command=added_value.degrees).grid(row=5,column=6,pady=1)
btnPow=Button(calc,text='Pow',width=6,height=2,font=('arial',20,'bold'),bd=4,bg='powder blue',command=added_value.power).grid(row=5,column=7,pady=1)

lblDisplay=Label(calc,text="Scientific Calculator",bg='purple',bd=40,fg='yellow',font=('algerian',25,'bold'),justify=CENTER)
lblDisplay.grid(row=0,column=4,columnspan=4)

r.mainloop()
