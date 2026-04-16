def arms(num):
    temp=num
    s=0
    while(num>0):
        digit=num%10
        s=s+(digit**3)
        num=num//10
    if (temp==s):
        print('armstrong')
    else:
        print('not armstrong')
n=int(input("enter a number:"))
arms(n)
