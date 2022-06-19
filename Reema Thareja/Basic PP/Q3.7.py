# WAP to prepare a grocery bill. For that enter the name of the item purchased, quantity and its price. Then display,
# *****************BILL*****************
# Item Name   Item Quantity   Item Price
# 
# ***************************************
# Total Amount to be Paid
# ***************************************

name=     str(input("Enter name of Item: "))
qty=float(input("Enter Quantity of Itme: "))
price=float(input("Enter Price: "))

total=qty*price

print("*****************BILL*****************")
print("Item Name\tItem Quantity\tItem Price")
print(name,"\t\t",qty,"\t\t",price)
print("**************************************")
print("Total amount to be paid: ",total)
print("**************************************")