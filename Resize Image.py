from tkinter import*
from PIL import Image
import sys
top=Tk()

top.title('Resize Image ')
top.config(bg='gray')
top.geometry('316x195')




def op():
   try:
      global file
      from tkinter.filedialog import askopenfilename
      root = Tk()
      root.withdraw()
      file = askopenfilename()
      
      global img
      img=Image.open(file)
      width,height=img.size
      out.set(width)
      out1.set(height)
   except:
      out2.set("Image Problem !")

def ok():
   w=int(e1.get())
   h=int(e2.get())
   img.thumbnail((int(w),int(h)))
   img.save("C:/Users/Komal Chaudhar/Desktop/Resize.jpg")
   out2.set("* Thank You *")

def show():
   img.show()

out=StringVar()
out1=StringVar()
out2=StringVar()
l=Label(text='<<< Resize your Images >>>',bg='gray',fg='yellow').place(x=80,y=0)
b=Button(text='Open >',bg='gray',fg='yellow',command=op).place(x=30,y=40)
l=Label(text='Width',bg='gray',fg='yellow',width='7').place(x=100,y=20)
l=Label(text='Height',bg='gray',fg='yellow',width='7').place(x=170,y=20)
ew=Entry(textvariable=out,width='8',fg='blue',justify='center').place(x=101,y=42)
eh=Entry(textvariable=out1,width='8',fg='blue',justify='center').place(x=171,y=42)

l=Label(text='Resize file :',bg='gray',fg='yellow',width='8').place(x=30,y=80)
e1=Entry(width='8',fg='blue',justify='center')
e1.place(x=101,y=80)
e2=Entry(width='8',fg='blue',justify='center')
e2.place(x=171,y=80)

b=Button(text='Ok',bg='gray',fg='yellow',command=ok).place(x=230,y=78)
b=Button(text='Show',bg='gray',fg='yellow',command=show).place(x=260,y=78)

e3=Entry(textvariable=out2,bg='gray',fg='white',width='15',justify='center').place(x=113,y=120)

l=Label(text=' /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/',bg='gray',fg='white').place(x=0,y=140)




l=Label(text='Change Image Extensions',bg='gray',fg='yellow').place(x=10,y=165)

var = StringVar(top)
var.set("Select ↓")

option = OptionMenu(top, var, "png", "jpg", "bmp", "gif", "pdf", "tif", "bat", "raw", "psd", "eps", "ai", "indd")
option.place(x=160,y=160)

def ok():
   try:
      img= Image.open(file)
      img.save("C:/Users/sande/Desktop/change."+var.get())
      out2.set("< Succesfull >")
   except:
      out2.set("Select Extension")

button = Button(top, text="Done",bg='gray',fg='yellow', command=ok)
button.place(x=255,y=163)


top.mainloop()
