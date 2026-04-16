n=int(input("enter limit"))
s=0
for i in range(n+1):
    if i%2==0:
        s+=i
print("sum=",s)
