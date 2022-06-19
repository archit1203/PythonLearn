"""A company decides to give bonus to all its employees on Diwali.
5% -> Male  10% -> Female
WAP to enter salary and sex of employee. If salary  > 10k then extra 2%
Calculate bonus and salary to be given"""
from numpy import ScalarType


male=0.05
female=0.10
ext=0.02
bonus=0
total=0

salary=float(input("Enter salary: "))
sex=input("Enter sex: (M for male and F for female)")
sex=sex.upper()
if sex == "M":
    bonus=male*salary
elif sex=="F":
    bonus=female*salary

if salary < 10000:
    bonus+=salary*ext

total=bonus+salary

print("Bonus is %d and Net Salary is %d" % (bonus,total) )
