x=0
y=1
n=int(input("enter limit:"))
count=0
if n==0:
    print("enter a positive number!!!")
elif n==1:
    print(x)
else:
    while count<n:
        print(x)
        z=x+y
        x=y
        y=z
        count+=1
        
