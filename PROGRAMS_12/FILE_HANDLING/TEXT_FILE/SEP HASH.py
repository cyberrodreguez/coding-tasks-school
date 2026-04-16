file=open("yoyo.txt","r")
lines=file.readlines()
for line in lines:
    words=line.split()
    for word in words:
        print(word,end="#")
    print()
file.close()
