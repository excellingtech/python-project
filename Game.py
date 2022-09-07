import random 
  
sum = 0
sum1 = 0
sum2 = 0
sum3 = 0
count = 0
flag = 0

while(1): 
      
    # generate random number at each turn 1-10 
    r1 = random.randrange(1,10) 
    r2 = random.randrange(1,10)
    r3 = random.randrange(1,10)
    r4 = random.randrange(1,10)
      
    # adding to account of players 
    sum = sum + r1 
    sum1 = sum1 + r2
    sum2 = sum2 + r3
    sum3 = sum3 + r4
    count = count+1
      
    print ("Total score of Sandy JI, pari %d is :  %d " % (count,sum)) 
    # break when player 1 reaches 100  
    if(sum>=100): 
      flag=1
      break
    
    print ("Total score of SAUMYA, pari %d is :  %d" % (count,sum1)) 
    # break when player 2 reaches 100  
    if(sum1>=100): 
      flag=2
      break
    
    print ("Total score of SHIVAM, pari %d is :  %d" % (count,sum2))   
    # break when player 2 reaches 100  
    if(sum2>=100): 
      flag=3
      break

    print ("Total score of VIAML, pari %d is :  %d" % (count,sum3))   
    # break when player 2 reaches 100  
    if(sum3>=100): 
      flag=4
      break
  
if(flag==1): 
   print("\nSandy JI wins the game")
elif(flag==2):
    print("\nSAUMYA wins the game")
elif(flag==3):
    print("\nSHIVAM wins the game")
else : 
   print("\nVIMAL wins the game")
