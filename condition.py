a=int(input("enter first number \n"))
b=int(input("enter second number \n"))
c=int(input("enter third number \n"))

if(a>b and a>c):
    print(f"{a} is the greatest")
elif(b>c and b>a):
    print(f"{b} is the greatest")
else:
    print(f"{c} is the greatest")
