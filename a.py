name = input('Please Enter Your First name:\n')
passwd = {'Mark' :'Tr678&.H',}
first = name.title()
if first in passwd:
  print("Hello,",first,"!", "The password is : ",passwd[first])
else:
  print("Hello,",first,"\b!", "See you later.")