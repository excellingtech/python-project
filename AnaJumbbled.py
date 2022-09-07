from tkinter import*
import random
from tkinter import messagebox

game=Tk()
game.geometry("500x500+400+120")
game.title("Anadrome Jumbbled")
lb=Label(text="ANADROME JUMBBLED",font=('Comic sans ms',25,'bold'),fg="brown",background="lightyellow")
lb.place(x=50,y=25)
game.config(background="orange")
game.resizable(width=False,height=False)

words=['typhon','vjaa','wifts','arms','bar','niktol','chin','care','ryque','arising',
             'adverb','katak','xlilgence','any','thiowalk','adomabrad','bamium','mega','mena','add',
             'colig','post','battle','unbred','teachers','coin','fare','felt','infests','genitals',
              'plug','heat','idle','inks','needless','liar','list','listen','smile','rule',
              'team','meteor','things','painter','near','swap','quiet','rape','rare','realist',
              'resque','viral','trees','split','serve','tried','vote','vines','wolves','wreathe']

answers=['python','java','swift','mars','bra','kotlin','inch','race','query','raising',
              'braved','katak','excelling','nay','kothiwal','moradabad','mumbai','game','name','dad',
              'logic','stop','tablet','burden','cheaters','icon','fear','left','fitness','stealing',
              'gulp','hate','lied','skin','lessened','rail','slit','silent','miles','lure',
              'mate','remote','nights','repaint','earn','wasp','quite','pear','rear','retails',
              'sequre','rival','reset','spilt','verse','tired','veto','veins','vowels','weather']

num=random.randrange(0,60)
def new():
    global words,answers,num
    num=random.randrange(0,60)
    label.config(text=words[num])
    e1.delete(0,END)

def default():
    global words,answers,num
    label.config(text=words[num])
    
def checkans():
    global words,answers,num
    var=e1.get()
    if var==answers[num]:
        messagebox.showinfo("Success",'This is the correct answer')
        new()
    else:
        messagebox.showerror("Error",'This is not the correct answer')
        e1.delete(0,END)

def Exit():
    game.destroy()
    exit()
    
label=Label(game,text="You're Welcome :-)",font=("Comic sans ms",22,"bold"),width=16,bg="blue",fg="yellow")
label.place(x=100,y=140)

ans=StringVar()

e1=Entry(game,font=("Comic sans ms",16,"bold"),bg='powder blue',fg='blue',textvariable=ans)
e1.place(x=115,y=200)

btnCheck=Button(game,text='Check',font=("Comic sans ms",16,'bold'),width=16,bg='green',fg='lime',command=checkans)
btnCheck.place(x=140,y=300)

btnNew=Button(game,text='New Word',font=("Comic sans ms",16,'bold'),width=16,bg='pink',fg='red',command=new)
btnNew.place(x=140,y=400)

btnExit=Button(game,text='Exit',font=("Comic sans ms",12,'bold'),width=4,bg='red',fg='yellow',command=Exit)
btnExit.place(x=450,y=460)

default()
game.mainloop()
