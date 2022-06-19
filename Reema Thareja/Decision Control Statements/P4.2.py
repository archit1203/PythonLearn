"""Change Oxford University Press to
oxford university press
OXFORD UNIVERSITY PRESS
oXFORD uNIVERSITY pRESS
"""
# str="Oxford University Press"
# print(str.upper())
# print(str.lower())
# print(str.swapcase())
"""Enter two numbers as dividend and divisor. If the divisor is greater than 0 then divide the dividend by
divisor. Assign their result to an integer variable rem and their quotient to a floating point number quo"""
# dvd=float(input("Enter: "))
# div=float(input("Enter: "))
# if div>0:
#     quo=dvd/div
#     rem=int(dvd%div)
# print("Quo: %f, Rem: %f"% (quo,rem))

"""WAP to prinit prime factors of a number"""
# n=int(input("Enter: "))
# for i in range(1,n):
#     if n%i==0:
#         print(i,end=" ")

"""WAP to print Floyyd's triangle
n=6
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
"""
# n=int(input("Enter: "))
# count=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(count,end=" ")
#         count+=1
#     print()

"""WAP to print sin(x) values where x rannges from 0 to 360 in steps of 15"""
import math
# PI=3.14
print(math.sin(math.pi/3))
angle=(math.pi/12)
twopi=(math.pi*2)
while(angle < (math.pi*2)):
    sine=math.sin(angle)
    print("sin(",angle,") = ",sine)
    angle=angle+(math.pi/12)
    """pi/3=60
        pi/12=15
        """