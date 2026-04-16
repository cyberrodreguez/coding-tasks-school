source=open("yoyo.txt","r")
a=source.read()
source.close()
dest=open("olo.txt","w")
q=dest.write(a)
dest.close()

