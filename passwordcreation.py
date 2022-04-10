##import string
##import random
##
##num=int(input("Enter length of password : "))
##uchar=string.ascii_uppercase
##lchar=string.ascii_lowercase
##digit=string.digits
##punct2="!@$%&*"
##password=""
##characters=uchar+lchar+digit+punct2
##for i in range(0,num):
##            password+="".join(random.choice(characters))
##print(password)
##


import string
import random

uchar=string.ascii_uppercase
lchar=string.ascii_lowercase
digit=string.digits
punct=string.punctuation

uchar1=random.choice(uchar)
lchar1=random.choice(lchar)
digit1=random.choice(digit)
punct1=random.choice(punct)

charater=uchar1+lchar1+digit1+punct1

password="".join(choice(charater) for i in range(0,4))
print(password)

