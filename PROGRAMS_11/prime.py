n=int(input("enter a number:"))
prime=True
i=2
while (i<=n//2):
    if(n%i==0):
        prime=False
        break
    i+=1
if(prime==True and n!=1):
    print("Prime number")
elif (n==1):
    print("neither prime nor composite number")
else:
    print("composite number")
