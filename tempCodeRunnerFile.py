salary=float(input())
# if salary <= 250000:
#     print("No Tax")
# elif salary>250000 and salary <= 500000:
#     print(salary*0.05)
# elif salary>500000 and salary <= 1000000:
#     print(salary*0.2)
# elif salary>1000000:
#     print(salary*0.3)
# else:
#     print("invalid tax")

# #2.MOVIE TICKET PRICING SYSTEM
# n=int(input("Enter:"))
# total=0
# for _ in range(n):
#     age = int(input())
#     if age>= 5 and age<=18:
#         total+=100
#     elif age>= 19 and age<=60:
#         total+=150
#     elif age>60:
#         total+=120
# print(total)


# #3.ELECTRICITY BILL GENERATOR
# units=int(input())
# bill=0
# if units<=100:
#     bill+=units*1.5
# elif units>100 and uits<=200:
#     bill+=150+(units-100)*2.5
# elif units>200 and units<=500:
#     bill+=400+(units-200)*4
# else:
#     bill+=1600+(units-500)*6
# print(bill)


# #4.CAR PARKING FEE CALCULATOR
# hrs=int(input())
# fees=0
# if hrs<=2:
#     print(30)
# elif hrs>2 and hrs<24:
#     fees = 30+(hrs-2)*10
# elif hrs>24:
#     print(200)


    

# #5.PRODUCT INVENTORY CHECKER (NESTED CONDITIONALS)
# name=input()
# qua=int(input())
# if qua==0:
#     print("Out Of Stock")
# elif qua>0 and qua<11:
#     print("LOw Stock")
# elif qua>10 and qua<51:
#     print("In stock")
# elif qua>50:
#     print("Overstocked")


# #6.pattern Row-wise Alternating 0 and 1
# n = int(input())
# for row in range(n):
#     for col in range(n):
#         if(row+col)%2==0:
#             print(0,end="")
#         else:
#             print(1,end="")
#     print()


# #7.GYM SUBSCRIPTION BILLING (MENU DRIVEN PROGRAM)
# while True:
# ch=int(input())
# ppl=int(input())
# if ch==1:
#     print(500*ppl)
# elif ch==2:
#     print(ppl*1300)
# elif ch==3:
#     print(ppl*5000)
# elif ch==0:
#     break
# else:
#     print("Invalid Choice")



# #8.BILLING BOT - APPLY DISCOUNT BASED ON AMOUNT
# total=float(input())
# if total<1000:
#     print(total)
# elif total>999 and total<5000:
#     print(total-total*0.05)
# elif total>4999 and total<10000:
#     print(total-total*0.1)
# elif total>=10000:
#     print(total-total*0.15)