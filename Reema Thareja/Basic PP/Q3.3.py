# WAP to calculate distance between 2 points
x1 = int(input("X1: "))
y1 = int(input("Y1: "))
x2 = int(input("X2: "))
y2 = int(input("Y2: "))

d = (((x2-x1)**2)+((y2-y1)**2))**0.5
print("Distance: ",d)