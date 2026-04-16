def count():
    f=open("yo.txt","r")
    count=0
    a=f.readlines()
    for i in a:
        k=i.split()
        for w in k:
            if w.lower()=="python":
                count+=1
    print("Python is occured",count,"times")
count()
