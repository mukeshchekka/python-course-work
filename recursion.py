def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
n=int(input("Enter the Value:"))
print(factorial(n))


def sumofnum(n):
    if n==1:
        return 1
    return n+sumofnum(n-1)
n=int(input("ENter the value:"))
print(sumofnum(n))


def shoot(n):
    if n==1:
        return 1
    shoot(n-1)
    print("After Recursion:",n)

def sumofdigits(n):
    if n==0:
        return 0
    return (n%10+sumofdigits(n//10)
print(sumofdigits(n))        


