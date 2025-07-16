#1.first program ============================================================================
# date=input()
# day,month,year=date.split("-")
# print(f"{year}/{month}/{day}")

#2.second program ============================================================================
# n=int(input())
# if n%2 == 0:
#     print("even number")
# else:
#     print("odd winner")

#3.Third program ============================================================================
# msg=input()
# vowels = "aeiouAEIOU"
# for v in vowels:
#     msg=msg.replace(v,"*")
# print(msg)

#4.Fourth Program ===========================================================================
# prices = list(map(float,input().split()))
# print(sum(prices))
# print(max(prices))

#5.Fifth program ==========================================================================
# credentials = ("admin","python123")
# username = input()
# password = input()
# if credentials[0] == username and credentials[1] == password:
#     print("login successful")
# else:
#     print("access denied")

#6.Sixth program =========================================================================
# names=input().split(',')
# unique_names=sorted(set(names))
# print(unique_names)

#7.Seventh Program =======================================================================
# n=int(input())
# marks_record={}
# for _ in range(n):
#     name,marks = input().split()
#     marks_record[name] = int(marks)
# topper = max(marks_record,key=marks_record.get)
# print(topper)

