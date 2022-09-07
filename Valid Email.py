import re
limit='^\w+()*(@\w{5,7})*(\.\w{2,3})+$'
def check(email):
   if(re.search(limit,email)):
      print("Valid Email")
   else:
      print("Invalid Email")

email=input('Enter Email to be checked= ')
check(email)
