pin=0000
cb=9000000
for i in range (3):
    p= int(input("Enter your pin:"))
    if p==pin:
        print("Correct pin")
        wb=int(input("Enter amount of Withdraw:"))
        if cb>wb:
            cb=cb-wb
            print("Transition Succesful!")
            print(cb,"Current balence")
        else:
            print("Insufficient Balance")
            print("Current Balance is",cb)
            print("You can try again")
        break
    else:
        print("Wrong Pin??")
else:
    print("Pin Locked")
 
