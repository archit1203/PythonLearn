"""WAP to print following pattern
* * * * *
*       *
*       *
*       *
* * * * *
*********
"""
# n=int(input(("Enter: ")))
# for i in range(1,n+1):
#     if i==1 or i==n:
#         print(n*"* ")
#     else:
#         print("*",end="")
#         print((2*n-3)*" ",end="")
#         print("*")

"""WAP to print following pattern
1 $ * * * *
2 * $     *
3 *   $   *
4 *     $ *
5 * * * * $
  123456789
(1,1)(2,3)(3,5)(4,7)(5,9)
"""
# n=int(input(("Enter: ")))
# for i in range(1,n+1):
#     for j in range(1,2*n):
#         if i==1 or i==n:
#             if (i==j and i==1) or (2*i-1)==j:
#                 print("$",end=" ")
#             elif j%2!=0:
#                 print("*",end=" ")
#         if i!=1 and i!=n:
#             if (2*i-1)==j:
#                 print("$",end="")
#             if j==1 or j==(2*n-2):
#                 print("*",end="")
#             else:
#                 print(" ",end="")
#     print()

"""WAP to print following pattern
1 $ * * * $
2 * $   # *
3 *   $   *
4 * #   $ *
5 $ * * * $
  123456789
  
1 $ * * * * * $
2 * $ * * * $ *
3 * * $ * $ * *
4 * * * $ * * *
5 * * $ * $ * *
6 * $ * * * $ *
7 $ * * * * * $
  1234566789ABC
  
(1,1)            (1,9)
    (2,3)    (2,7)
        (3,5)
    (4,3)    (4,7)
(5,1)            (5,9)

(1,1)                    (1,13)
    (2,3)           (2,10)
        (3,5)   (3,8)
            (4,6)    
        (5,5)   (5,8)     
    (6,3)           (6,10)
(7,1)                     (7,13)

"""
n=int(input(("Enter: ")))
for i in range(1,n+1):
    for j in range(1,2*n):
        if i==1 or i==n:
            if j==1 or j==(2*n-1):
                print("$",end=" ")
            elif j%2!=0:
                print("*",end=" ")
        if i!=1 and i!=n:
            if (2*i-1)==j :
                print("$",end="")
            if j==1 or j==(2*n-2):
                print("*",end="")
            else:
                print(" ",end="")
    print()