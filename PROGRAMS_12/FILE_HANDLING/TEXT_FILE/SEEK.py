def seek_file():
    f=open("yo.txt","r")
    f.seek(16)
    data=f.read()
    print("content of the data=",data)
    f.close()
seek_file()
