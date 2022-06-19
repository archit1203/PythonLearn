"""
Calculate tax in given conditions:
if income < 150,000 then no tax
if income is 150001 - 300,000 then 10%
if income is 300001 - 500,000 then 20%
if income >  500001 30%
"""
MIN1= 150000
MIN2= 150001
MAX1= 300000
MIN3= 300001
MAX2= 500000
MIN4= 500001

T1=0
T2=0.1
T3=0.2
T4=0.3

income=int(input("Enter: "))
ti=income-150000

if ti <= 0:
    print("No Tax")
elif ti>=MIN2 and ti<MAX1:
    tax=(ti-MIN2)*T1
    print("Tax = ",tax)
elif ti>=MIN3 and ti<MAX2:
    tax=(ti-MIN3)*T2
    print("Tax = ",tax)
elif ti>=MIN4:
    tax=(ti-MIN4)*T3
    print("Tax = ",tax)
