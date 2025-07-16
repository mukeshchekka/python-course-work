#STRINGS

#Defining strings
str1 = 'Hello'
str2 = 'world'
str3 = 'string declaration'
print(str1)
print(str2)
print(str3)
#Output:
'''Hello
world
string declaration'''

#Operations on strings
#1.Concatenation
str1 = "Hello"
str2 = "world"
str3 = str1+" "+str2
print(str3)
#Output:
'''Hello world'''

#2.Repetition
print("Python!"*3)
#output:
'''Python!Python!Python!'''

#3.Indexing
text = "python"
print(text[0])  #ouput: p (prints first character),(indexing starts from 0)
print(text[-1])#output : n (prints last character)

#4.Slicing
print(text[0:3])#output: pyt (from index 0 to 2)
print(text[:4]) #output: pyth (default start is 0)
print(text[2:])#output: thon (from index 2 to end)

#5.Membership
print('pyt' in text) #output : True
print('java' not in text) #output : True
