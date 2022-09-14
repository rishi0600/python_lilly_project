print('hello')
from datetime import date
from getopt import gnu_getopt
from turtle import hideturtle

a=input('Hi, what is your First Name')
b=input('last Name')
Name=("{0} {1}".format(a,b))
c=input('what is your DOB')
e=int(c.split("-")[2])
Age=date.today().year-e
mail=input("what is your mail")
mob=int(input("wts ur contact"))
city=input("wts ur city")
country=input("which country?")
Bg=input('your blood group?')
print("Hello {0} your age is {1}".format(Name,Age))
print("Mail=",mail)
print("contact=",mob)
print("city=",city)
print("country=",country)
print("bloodgroup=",Bg)