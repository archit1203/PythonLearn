"""Calculate electricity bill based on following
Unit    Charge
0-150   3/u
151-350 100+3.75/u after 150
301-450 250+4/u after 350
451-600 300+4.25/u after 450
600+    400+5/u after 600"""
# unit=int(input("Enter: "))
# chg=0
# if unit<151:
#     chg=unit*3
# elif unit>150 and unit<351:
#     chg=100+ (3.75*(unit-150))
# elif unit>300 and unit<451:
#     chg=250+ (4*(unit-350))
# elif unit>450 and unit<600:
#     chg=300+ (4.25*(unit-450))
# elif unit>=600:
#     chg=400+ (5*(unit-600))
# print("Charge= ",chg,"For ",unit,"units")

"""WAP to read angle from user and display its quadrant"""
# angle=float(input("Enter in degrees: "))
# if angle>=0 and angle<=90:
#     print("I")
# if angle>90 and angle<=180:
#     print("II")
# if angle>180 and angle<=270:
#     print("III")
# if angle>270 and angle<=360:
#     print("IV")

"""WAP that accepts the current date and dob of user.Then display the age of user (dd/mm/yy)"""
# cur_date=int(input("Enter today's date: "))
# cur_month=int(input("Enter current month: "))
# cur_year=int(input("Enter current year: "))
# print()
# dob_date=int(input("Enter birth date: "))
# dob_month=int(input("Enter birth month: "))
# dob_year=int(input("Enter birth year: "))
# age_year=cur_year-dob_year
# if cur_month>dob_month:
#     age_month=cur_month-dob_month
# else:
#     age_month=dob_month-cur_month
# if cur_date>dob_date:
#     age_date=cur_date-dob_date
# else:
#     age_date=dob_date-cur_date
# print(age_date,"days",age_month,"moths",age_year,"years")

"""WAP to display all numbers between 1-100 that are not divisble by 2 or 3"""
# for i in range(1,101):
#     if i%2==0 or i%3==0:
#         continue
#     else:
#         print(i)

"""WAP to calculate parking charges of a vehicle. Enter type of vehicle as a charecter and the number 
of hours the calculate as per below:
Truck/bus: 20/hr
Car: 10/hr
2 wheeler: 5/hr"""
# type=input("Press T for truck,bus\nPress C for car\nPress S for 2 Wheeler\nEnter type of vehicle: ")
# hrs=int(input("Enter hours: "))
# type=type.upper()
# chg=0
# if type=="T":
#     chg=hrs*20
# elif type=="C":
#     chg=hrs*10
# elif type=="S":
#     chg=hrs*5
# else:
#     print("Error")
# if chg:
#     print("Pay Rs. ",chg)

"""WAP to print the table of sin and cos in range 0-360 in increments of 15"""
# import math 
# print("Sine series is as shown below\n") 
# for i in range(0,361,15):
#     x=math.radians(i) 
#     y=math.sin(x)
#     z=math.cos(x)
#     print("sine", i ,": %.4f"%y,"\tcos", i ,": %.4f"%z) 
#     if i%90==0 and i!=0:
#         print("------------------------------")
# print("Finished printing the sine series for a given range")

"""Sum of all odd numbers between 1 and 100"""
# sum=0
# for i in range(1,101):
#     if i%2!=0:
#         sum=sum+i
# print("SUM: ",sum)

"""WAP an interactive program to read an integer. If it is positive then displlay corresponding 
binary equivalent. Enter 999 to stop. If input -ve then ask to renter"""
# while(1):
#     n=int(input("Enter number or 999 to quit: "))
#     if n==999:
#         print("End of loop")
#         break
#     if n>0:
#         print(bin(n))
#     else:
#         print("Enter a positive number: ")
#         continue

"""WAP that accepts any number and diplays its number of digits"""
# count=0
# n=int(input("Enter: "))
# while(n>0):
#     n=int(n/10)
#     count+=1
# else:
#     print("Digits= ",count)