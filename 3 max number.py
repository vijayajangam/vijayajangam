x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
z=int(input("Enter third number:"))
if x>y and x>z:
    print(x,"is greater")
elif y>x and y>z:
    print(y,"is greater")
elif z>x and z>y:
    print(z,"is greater")
else:
    print("all are equal")
