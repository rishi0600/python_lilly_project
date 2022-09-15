import cal

a=input("wts ur firstname")
b=input("wts your lastname")
print("Name:{0} {1}".format(a,b))

s=cal.take_salary()
u=cal.HRA(s)
v=cal.DA(s)
w=cal.Bonus(s)

totalsal=float(s)+float(u)+float(v)+float(w)
print("Your Total salary =",totalsal)
