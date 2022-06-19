# Armstrong number
# num=int(input("Enter: "))
# sum=0
# n=num
# while(num>0):
#     rem=num%10
#     sum=sum+(rem**3)
#     num=num//10
# if sum==n:
#     print("Yes")
# else:
#     print("No")

"""
n=10
n/2=5   rem=1
n/2=2   rem=1
n/2=1   rem=0
n/2=0   rem=0
"""
# WAP to enter the decimal number and display its binary equivalent
n=int(input("Enter : "))
# # b=bin(n)
# # print("Binary %d = "%n , b)
# rem=0
sum=0
i=0
print("A")
while(n!=0):
    rem=n%2
    print(rem)
    sum=sum+rem*(10**i)
    n=n/2
    i=i+1
    print(n)
print(sum)

# Function to print binary number using recursion
def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

# decimal number
dec = int(input("Enter : "))
convertToBinary(dec)