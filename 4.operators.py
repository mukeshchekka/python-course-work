#1.Arithmetic operators
a=10
b=20
print("addition(+):",a+b)
print("substraction(-):",a-b)
print("Multiplication(*):",a*b)
print("Divison(/):",a/b)
print("FloorDivision(//):",a//b)
print("Modulus(%):",a%b)
print("exponent(**):",a**b)

#2.Comparision operators
a=20
b=10
print("EqualTo(==):",a==b)
print("NotEqualTo(!=):",a!=b)
print("GreaterThan(>):",a>b)
print("LessThan(<):",a<b)
print("GreaterThanEqualTo(>=):",a>=b)
print("LessThanEqualTo(<=):",a<=b)

#3.Assignment Operators
x=10

print("Assign(=):",x)# Assigns value to a variable
x+=3  # (x += 3) means (x = x + 3)
print("Add & Assign(+=) :", x) 
x-=2   # (x -= 2) means (x = x - 2)
print("Subtract & Assign(-=):", x)
x*=4   # (x *= 4) means (x = x * 4)
print("Multiply & Assign(*=):", x)
x/=2  #(x /= 2) means (x = x / 2)
print("Divide & Assign(/=):", x )
x//=3   # (x //= 3) means (x = x // 3)
print("Floor Divide & Assign(//=):", x)
x%=2   # (x%=  2) means (x = x % 2)
print("Modulus & Assign(%=):", x)
x**=3   #( x **= 3) means (x = x ** 3)
print("Exponentiate & Assign(**=):", x)

#4. Logical Operators
'''Operator Symbol Example Explanation
AND and (x > 5 and y <15) ----> Returns True if both conditions are true
OR or (x < 5 or y > 15) ----> Returns True if at least one condition is true
NOT not not (x > 5) ------> Reverses the condition (True becomes False)'''
a=30
b=10
print(a%10 == 0 and b%10 == 0)
print(a%5 == 0 or b%10 == 0)



#5. Membership operators
names = ['rahul','manish','mukesh','tarak']
print('in result:','rahul' in names )  #in result : True
print('in result:','rahul' not in names ) #in result : False


#6.Identity Operators
l = [1,2,3,4]
b = [1,2,3,4]
a=b #Assign b to a
print("l is b:",l is b) #l is b: False      
print("a is b :",a is b) #a is b: True
print("id(l):",id(l))  #id(l):1903465934400
print("id(a):",id(a))  #id(a):1903465555712
print("id(b):",id(b))  #id(b):1903465555712
print("a is not b:",a is not b)#a is not b:False
print("l is not b:",l is not b)#l is not b:True


#7. Bitwise operators
x=5 #Binary : 0101
y=3 #Binary : 0011
print(x&y) #1
print(x|y) #7
print(x^y) #6
print(~y) #-4
print(x<<y) #40
print(x>>y) #0





