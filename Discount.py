#discount
def dis():
    a=int(input("enter the price= "))
    d=int(input("enter the discount= "))
    b=(a*d)/100
    print("your discount= ", b)
    f=a-b
    print("final price= ",f)
dis()
