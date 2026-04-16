def file_tell():
    f=open("yo.txt","r")
    f.seek(10)
    data=f.read(3)
    position=f.tell()
    print("content=",data)
    print("position=",position)
    f.close()
file_tell()
           
