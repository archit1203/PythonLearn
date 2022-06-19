# SI = PRT/100
# CI = P (1+(r/n)/100)^nt 
p=float(input("P: "))
r=float(input("R: "))
t=float(input("T: "))
n=float(input("N: "))
r=r/100
si=(p*r*t)
ci=p*((1+r)**t)-p
# ci=p*((1+((r/n)/100))**(n*t))

print("SI= ",si,"\nCI= ",ci)