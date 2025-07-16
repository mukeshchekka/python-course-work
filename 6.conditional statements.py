'''#conditional statements
#using dictionaries
data = {'mukesh@gmail.com':'123@123','rahul@gmail.com':'456@456','pawan@gmail.com':'789@789'}
email,pwd = input("enter the email and pwd:").split()
if data.get(email) == pwd:
    print("pass")
else:
    print("fail")
    break:'''
    

#using list
items=['coffee','icecream','samosa','idly']
stocks=[20,50,40,0]
data=input("enter the item:")
if data in items:
    ind = items.index(data)
    if stocks[ind]>0:
        print("ava")
    else:
        print("not ava")
else:
    print("item not ava")
