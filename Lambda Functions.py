a=20
divl = lambda a,b = 3: a/b
print(divl(a))


squ = list(map(lambda i:i**2,l))
print(squ)

l='python'
v='aeiouAEIOU'
squ = list(map(lambda i:'*' if i in v else i ,l))


d = dict(sorted(data.items(),key = lambda i:i[i],reverse=True))
print(d)
