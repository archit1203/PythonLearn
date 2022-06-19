# """
# WAP to calculate the value of investment. Input initial value, annual interest and calculate value of 
# investment over time
# """
# init=float(input("Enter: "))
# rate=float(input("Enter: "))
# year=int(input("Enter: "))

# final= init
# for i in range(1,year+1):
#     final=final * (1+rate/100.0)

# print(final)

# WAP to genertae a calaender given start day and number of days
start=int(input("Enter start day (1-7): "))
num=int(input("Enter num of days: "))
print("Sun\tMon\tTue\tWed\tThur\tFri\tSat")
print("----------------------------------------------------------")
for i in range(start-1):
    print(end="\t\t\t\t")
    i=start-1
    for j in range(1,num+1):
        if(i>6):
            print()
            i=1
        else:
            i=i+1
        print(str(j) + "\t" ,end=" ")