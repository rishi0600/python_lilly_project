
def take_salary():
    salary=int(input("What is your Salary?"))
    print("Your Salary:",salary)
    return(salary)

def HRA(salary):
    hra=0.4*salary
    print("your hra:",hra)
    return(salary)

def DA(salary):
    da=0.3*salary
    print("your da is:",da)
    return(salary)

def Bonus(salary):
    bonus=0.1*salary
    print("your bonus is:",bonus)
    return(salary)
    
