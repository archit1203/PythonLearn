"""WAP to substract two numbers via function"""
# def subs(x,y):
#     return x-y

# n=int(input("Enter: "))
# m=int(input("Enter: "))
# print(subs(n,m))

"""display strings repetedly"""
# def disp(x):
#     for i in range (0,4):
#         print(x)

# s="Archit"
# disp(s)

"""Error in func call"""
# def func(i,j):
#     print(i,j)

# func(5)
# # Traceback (most recent call last):
# #   File "g:\KIET\Programming\NewCode\Python\Reema Thareja\Functions and Modules\Q5.1.py", line 20, in <module>
# #     func(5)
# # TypeError: func() missing 1 required positional argument: 'j'

"""Error in func call"""
# def func(j):
#     print(i,j)

# func(5,5)
# # Traceback (most recent call last):  
# File "g:\KIET\Programming\NewCode\Python\Reema Thareja\Functions and Modules\Q5.1.py", line 31, in <module>
#     func(5,5)
# TypeError: func() takes 1 positional argument but 2 were given

"""local and global variable"""

# num1=10
# print("Global variable= ",num1,"num1")
# def func(num2):
#     print("Local var in function = ",num2)
#     num3=30
#     print("Local var in function = ",num3)

# func(20)
# print("num1 again ",num1)
# # Traceback (most recent call last):
# #   File "g:\KIET\Programming\NewCode\Python\Reema Thareja\Functions and Modules\Q5.1.py", line 48, in <module>
#     # print("num3 outside scope: ",num3)
# # NameError: name 'num3' is not defined. Did you mean: 'num1'?
# print("num3 outside scope: ",num3)


"""GLobal Statement"""
var="Good"
def show():
    global var1
    var1="Morning"
    print("in function var is ",var1)

show()
print("outside function var1 is ",var1)
print(" var is ",var)