# # # Avg of first n natural numbers
# # n=int(input("Enter: "))
# # sum=avg=0
# # for i in range(n+1):
# #     sum+=i
# # avg=float(sum/n)
# # print("AVG = ",avg)

# # Multiplication table of n
# # n=int(input("Enter: "))
# # for i in range(1,11):
# #     print("%d x %d = %d"% (n,i,n*i))

# # Factorial
# # n=int(input("Enter: "))
# # fact=1
# # if n==0 or n==1:
# #     print(1)
# # else:
# #     for i in range(1,n+1):
# #         fact=fact*i
# # print(fact)

# # Prime or composite
# n=int(input("Enter: "))
# flag=0
# for i in range(2,n):
#     if n%i==0:
#         flag=1
#         break
# if n==1:
#     print("Nothing")
# if flag:
#     print("Composite")
# else:
#     print("Prime")

# # WAP to print sum of series: 1 + 1/2 + ...... + 1/n
# n=int(input("Enter: "))
# sum=0.0
# for i in range(1,n+1):
#     a=1.0/i
#     sum=sum+a
# print("SUM: ",sum)

# WAP to print sum of series: 1 + 1/2^2 + ...... + 1/n^2
# n=int(input("Enter: "))
# sum=0.0
# for i in range(1,n+1):
#     a=1.0/(i**2)
#     sum=sum+a
# print("SUM: ",sum)

# # Sum of cubes from 1 to n
# n=int(input("Enter: "))
# sum=0
# for i in range(1,n+1):
#     sum=sum+(i**3)
# print(sum)

# Print sq of even numbers
# n=int(input("Enter: "))
# sum=0
# for i in range(1,n+1):
#     if i%2==0:
#         sum=sum+(i**2)
# print(sum)