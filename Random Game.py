'''import random

for i in range(1,5,1):
   a=int(input('Enter a num= '))
   d=random.randrange(1,5)
   if (a==d):
      print('Winner Winner Chickan Dinner')
      break
   else:
      print("Play again")
      
print(d)'''


import random
z=int(input('Enter Limit= '))
d=random.randrange(1,z)
for i in range(0,z,1):
   a=int(input('Enter a num= '))
   if(a<=z):
      if (a<d):
         print("Too small")
      elif(a>d):
         print("Too Big")
      else:
         print('Winner Winner Chickan Dinner')
         break
   else:
      print("Wrong Value")
      break
print(d)
