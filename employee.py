a=int(input())
b=int(input())
if a>=10:
    b=b*1.15
    print(b)
elif a>=5 and a<10:
    b=b*1.1
    print(b)
elif a>=3 and a<5:
    b=b*1.05
    print(b)
else:
    print("not eligible")