n=int(input("enter a number"))
temp=n
s=0
while (n>0):
    digit=n%10
    s=s+(digit**3)
    n=n//10
if (temp==s):
    print("Armstrong number")
else:
    print("not Armstong number")        

    

