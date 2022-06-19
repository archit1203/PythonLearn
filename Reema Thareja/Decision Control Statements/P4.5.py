"""WAP to print following pattern
1 8 27 64...........
-5 -2 0 3 6 9 12........
-2 -4 -6 -8 -10 -12............
1 4 7 10...........
"""
# n=int(input("Enter: "))
# # n=4
# for i in range(1,n+1):
#     print(i**3,end=" ")
# print()
# print("-5 -2 ",end="")
# for i in range(0,n*3+1,3):
#     print(i,end=" ")
# print()
# for i in range(-2,-n*3-1,-2):
#     print(i,end=" ")
# print()
# for i in range(1,n*3+1,3):
#     print(i,end=" ")
# print()

"""WAP to print patter:
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
n=5
"""
# n=int(input("Enter: "))
# for i in range(5):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

"""WAP to print patter:
1
2 1 2
3 2 1 2 3
"""
# n=int(input("enter: "))
# for i in range(1,n+1):
#     for j in range(i,1,-1):
#         print(j,end=" ")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print() 

"""WAP the pattern
n=12345

12345    1
 2345    12
  345    123
   45    1234
    5    12345
"""
n=int(input("Enter: "))
x=int(len(str(n)))
# print(x)
# x=5
y=x
sum=0
for i in range(1,x+1):
    rem=n%(10**y)
    y-=1
    sum=int(n/(10**(x-i)))
    print(rem,"\t",sum)