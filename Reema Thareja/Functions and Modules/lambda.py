"""
Lambda Function
->Throwaway functions
->syntax:   lamda arguments : expression
-> ',' seprates the arguments
-> 
"""

"""Eg 1"""
# sum = lambda x , y : x+y

# print("Sum: ",sum(2,3))

# def sumdif(x,y):
#     sm=a+b
#     dif=a-b
#     return sm*dif

# a = int(input())
# b = int(input())

# print(sumdif(a,b))



def solve(n):
    for i in range(1,n+1):
        for k in range(1,i+1):
            print(k,end="")
        for l in range(i-1,0,-1):
            print(l,end="")
        print("\n")
    
solve(5)