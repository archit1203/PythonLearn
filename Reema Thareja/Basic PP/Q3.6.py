# WAP to calculate salary of an employee given his basic pay, HRA=10% of basic pay, 
# TA=5% of basic pay, Define HRA and TRA as constants and 
# use them to calculate he salary of the eomplyee


pay=float(input("Enter: "))
hra=0.1
ta=0.05
salary=pay+(hra+ta)*pay
print(salary)
