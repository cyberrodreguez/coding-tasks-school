def count():
    f=open("yo.txt","r")
    text=f.read()
    space=line=char=0
    for i in text:
        if(i==''):
            space+=1
        elif(i=="\n"):
            line+=1
        else:
           char+=1
    f.close()
    print("spaces=",space)
    print("lines=",line+1)
    print("characters=",char)
count()
