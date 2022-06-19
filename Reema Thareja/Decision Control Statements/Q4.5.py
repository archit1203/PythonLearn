# #WAP to print first 10 numbers
# for i in range (0,11):
#     print(i,end=" ")

# #WAP to print first 10 numbers seprated by tab
# for i in range (0,11):
#     print(i,end="\t")

# WAP to print sum and average of first 10 nunmbers
# i=0
# sum = 0
# avg = 0
# while(i<=10):
#     sum=sum+i
#     i=i+1

# avg=float(sum)/10
# print("Sum = %d \nAverage = %.2f"% (sum,avg))

# WAP to print 20 horizont astricks
# i=1
# while(i<=20):
#     print("*",end="")
#     i+=1

# WAP to calculate sum of numbers from m to n
# m=int(input("Enter m: "))
# n=int(input("Enter n: "))
# i=0
# while(m<=n):
#     i=i+m
#     m+=1

# print("Sum= %d"%i)

# WAP to read number until -1 encountered, also count no of +ve, -ve and 0s
# p=n=z=0
# while(1):
#     num=int(input("Enter number or -1 to exit: "))
#     if num==-1:
#         break

#     if num==0:
#         z+=1
#     elif num>0:
#         p+=1
#     else:
#         n+=1

# print("Number of Negatives = ",n)
# print("Number of Zereos    = ",z)
# print("Number of Positives = ",p)

# WAP to read number until -1 encountered, find average of +ve and -ve numbers
p=n=0
psum=nsum=0
while(1):
    num=int(input("Enter number or -1 to exit: "))
    if num==-1:
        break

    if num>0:
        p+=1
        psum+=num
    else:
        n+=1
        nsum+=num

print("Average of Negatives = ",nsum/n)
print("Average of Positives = ",psum/p)