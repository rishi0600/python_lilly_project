num=input("mob?")
name=input("name?")
age=int(input("age?"))
salary=int(input("salary?"))
if len(num)>10:
    print("Enter a valid number")
else:
    print(num)


if len(name)<=0:
    print("type ur name")
else:
    print(name)

if age>=18:
    print(age)
else:
    print("u r not eligible")

if salary<0:
    print("enter ur salary")
else:
    print(salary)
    
