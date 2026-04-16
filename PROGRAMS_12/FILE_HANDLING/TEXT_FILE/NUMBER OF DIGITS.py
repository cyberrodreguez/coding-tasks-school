def dig():
    f=open("yo.txt","r")
    digit=f.read()
    count=0
    for i in digit:
        if(i.isdigit()):
            count+=1
    f.close()
    print("Number of digits=",count)
dig()

