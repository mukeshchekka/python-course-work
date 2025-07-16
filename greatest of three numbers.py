a=int(input("Enter a: "))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
if a>b and a>c:
    print(f"{a} is the greatest number")
elif b>a and b>c:
    print(f"{b} is the greatest number")
elif a==b==c:
    print("All numbers are equal")
else:
    print(f"{c} is the greatest number")
