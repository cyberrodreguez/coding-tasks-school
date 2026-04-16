n=int(input("Enter a number:"))
if n<0:
    print("invalid number")
elif n>=0:
    if n<10:
        print("one digit")
    elif n<100:
        print("two digit")
    elif n<1000:
        print("three digit")
    else:
        print("high")

else:
    None
