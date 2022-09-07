# Grade calculater
def h():
    data=[]
    t=int(input("The M.M.= "))
    d=int(input("Enter the Total sub.= "))
    for i in range (1,d+1,1):
        print(f'Enter the {i} sub. no.= ')
        get=int(input())
        if(get<t or get==t):
            data.append(get)
        else:
            print("Wrong Value")
            break
    print("The Marks list is- ",data)
    if((len(data))==d):
        s=sum(data)
        print("Your Total no.= ",s)
        c=(s*100)/(t*d)
        p=round(c,2)  #take only two .numbers
        if(p>100):
            print("ERROR...")
        elif(p>=90):
            print(p,"& Topper")
        elif(p>=60):
            print(p,"& 1st Rank")
        elif(p>=40):
            print(p,"& 2nd Rank")
        else:
            print(p,"& Fail")
    else:
        print("SomeThing Went Wrong!!!")
h()

