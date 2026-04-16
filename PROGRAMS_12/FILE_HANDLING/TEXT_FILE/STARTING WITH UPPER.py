def display():
    f=open("yoyo.txt","r")
    k=f.readlines()
    for line in k:
         if line[0].isupper():
             print(line)
display()
