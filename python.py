from operator import truediv


num=input("Enter your mob?")
while len(num)!=10 or num.isnumeric()==False:
    num=input("Enter a valid number")  
print(num)

name=input("What is your name?")
while len(name)<=0 or name.isalpha()==False:
    name=input("type ur name")

print(name)

age=(input("your age?"))
while age.isnumeric()==False or int(age)<20 or int(age)>99:
      age=input("Enter correct age")
print(age)

salary=input("wt is the salary?")
while len(salary)<=0 or salary.isnumeric()==False:
    salary=input("Enter Valid salary: ",)
print(salary)

city=input("Enter your city: ")
while city.isalpha()==False or len(city)<=0:
    city=input("Enter valid City name: ")
print(city)
    
department=input("Enter Your Department: ")
while len(department)==0 or department.isalpha()==False:
    department=input("Enter Valid Department: ")
print(department)

    
print("Name=",name)
print("contact number=",num)
print("Age=",age)
print("Salary=",salary)
print("City=",city)
print("Department=",department)
