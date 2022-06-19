# # WAP to print
# """
# PASS 1- 1 2 3 4 5
# PASS 2- 1 2 3 4 5
# PASS 3- 1 2 3 4 5
# PASS 4- 1 2 3 4 5
# PASS 5- 1 2 3 4 5
# """
# for i in range(1,6):
#     print("PASS %d- "%i,end=" ")
#     for j in range(1,6):
#         print(j,end=" ")
#     print()

# """WAP to print
# **********
# **********
# **********
# **********
# **********
# """
# n=int(input("Enter: "))
# for i in range(n):
#     print(2*n*"*")

"""WAP to print
*
**
***
****
*****
# """
# n=int(input("Enter: "))
# for i in range(1,n+1):
#     print(i*"*")

# """WAP to print
# 1
# 1 2
# 1 2 3
# 1 2 3 4 
# 1 2 3 4 5
# """
# n=int(input("Enter: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# """WAP to print
# 1
# 22
# 333
# 4444
# 55555
# """
# n=int(input("Enter: "))
# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end=" ")
#     print()

# """WAP to print
# 0
# 12
# 345
# 6789
# """
# n=int(input("Enter: "))
# count=0
# for i in range(1,n):
#     for j in range(1,i+1):
#         print(count,end="")
#         count+=1
#     print()

"""WAP to print
    1
   21
  321
 4321
54321
"""
# n=int(input("Enter: "))
# for i in range(1,n+1):
#     for k in range(5,i,-1):
#         print(" ",end='')
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

"""WAP to print
        1
      1 2 1
    1 2 3 2 1
  1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
"""
n=int(input("Enter: "))
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",end=' ')
    for k in range(1,i+1):
        print(k,end=" ")
    for l in range(i-1,0,-1):
        print(l,end=" ")
    print()

