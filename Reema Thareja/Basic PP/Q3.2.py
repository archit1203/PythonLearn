#Calcluate Area of triangle using Heron's Formula
# ar= sqrt {S*(S-a)*(S-b)*(S-c)}

a=float(input("A: "))
b=float(input("B: "))
c=float(input("C: "))
S=(a+b+c)/2
ar = (S*(S-a)*(S-b)*(S-c)) ** 0.5
print(ar)