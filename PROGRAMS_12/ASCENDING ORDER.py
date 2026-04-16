a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter a third number"))
min=mid=max=None
if a<b and a<c:
    if b<c:
        min,mid,max=a,b,c
    else:
        min,mid,max=a,c,b
elif b<a and b<c:
    if a<c:
        min,mid,max=b,a,c
    else:
        min,mid,max=b,c,a
else:
    if a<b:
        min,mid,max=c,a,b
    else:
        min,mid,max=c,b,a
print("numbers in ascending order",min,mid,max)
