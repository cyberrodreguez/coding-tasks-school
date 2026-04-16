count=int(input("How many students are there in the class"))
fileout=open("marks.txt","a")
for i in range(count):
    print("Enter the details for students",(i+1),"below")
    rollno=int(input("Roll No"))
    name=input("Name")
    marks=int(input("Marks"))
    rec=str(rollno) + ',' + name + ',' + str(marks) + '\n'
    fileout.write(rec)
fileout.close()

    

