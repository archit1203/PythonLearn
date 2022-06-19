# WAP to count number of lower case, uppercase and digits entered
# str=input("Enter: ")
# lcount=ucount=dcount=0
# for i in str:
#     if i.isupper():
#         ucount+=1
#     elif i.islower():
#         lcount+=1
#     elif i.isdigit():
#         dcount+=1
# print("Lower= %d, Upper= %d, Digits= %d"% (lcount,ucount,dcount))

"""Correct number 99"""
# print("Let's Begin")
# flag=0
# while(1):
#     n=int(input("Enter number: "))
#     if n >99:
#         print("Enter Lower")
#         continue
#     elif n<99:
#         print("Enter Bigger")
#         continue
#     elif n==99:
#         flag=1
#         break
# if flag:
#     print("You gussed it right")

"""WAP that prints a number , its square annd cube repeatedly in the range (1,n)"""
# n=int(input("Enter: "))
# for i in range(1,n+1):
#     sq=i**2
#     cube=i**3
#     print("Number: %d, Square: %d, Cube: %d"% (i,sq,cube))

"""WAP that prompts the user to enter a string. The program calculates and displays the length of string
until the user enters "QUIT"""
# while(1):
#     count=0
#     str=input("Enter string: ")
#     if str=="QUIT":
#         break
#     for i in str:
#         count+=1
#     print("Length of this string is %d"%count)

"""wap that prompts the user to enter five words. If length of any word is less than 6 characters, 
then it asks thee user to enter it again. However, if the word is of 6 or more characters, 
then it displays it on the screen Reema Thareja"""

# words = [ ]
# n = int(input("Enter number of elements : "))
# for i in range(0, n):
# 	ele = [input()]
# 	words.append(ele)
	
# # print(words)
# # for i in range(n):
#     # words[i]=input("Enter: ")
# print(type(words[1]))
# for i in words:
#     for j in i:
#         j=str(j)
#         if len(j)<6:
#             print(type(j), len(j))
#             # words[i]=input("Enter again: ")
#         else:
#             print(words[i])

str=input("Enter: ")
ch=""
count=0
for i in str:
    # print(i,end=" ")
    ch=ch+i
    count=count+1
    if i.isspace() or i==str[-1]:
        if count<6:
            pass
        print(ch)
        ch=""
        count=0
