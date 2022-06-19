"""WAP to print calender of any year"""
import calendar as cl
y=int(input("Enter year: "))
print("-----------------------------------")
Cal=cl.TextCalendar(cl.SUNDAY)
i=1
while i<=12:
    cl.prmonth(y,i)
    i+=1