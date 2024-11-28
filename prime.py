x=int(input("Enter a number:"))
for i in range (2,x):
    if x%i==0:
        print(x,"is not prime")
        break
else:
    print(x,"is a prime number")
