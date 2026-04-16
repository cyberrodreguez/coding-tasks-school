f=open("yo.txt","r")
count=0
rec=''
while True:
    rec=f.readline()
    if rec=='':
        break
    count+=1
    print(count,rec,end='')
f.close
