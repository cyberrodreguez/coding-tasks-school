
import pickle
'''stu={}
stufile=open('stu.dat','wb')
ans='y'
while ans.lower()=='y':
    rno=int(input("enter roll number"))
    name=input("Enter name")
    marks=int(input("Enter marks"))
    stu["Roll Number"]=rno
    stu["Name"]=name
    stu["Marks"]=marks
    pickle.dump(stu,stufile)
    ans=input("Do you want to enter more records?(y/n)")
stufile.close()

f=open("stu.dat","rb")
try:
    print("*******************************STUDENT DETAILS**********************************")
    while True:
        print(pickle.load(f))
except EOFError:
    f.close() '''   

stu=[]
f=open("stu.dat","rb")
while True:
    try:
        stu=pickle.load(f)
    except EOFError:
        break
ans="y"
while ans.lower()=="y":
    found=False
    r=input("Enter the roll number to search")
    for s in stu:
        if s["Marks"]==r:
            print(s)
            found=True
            break
    if not found:
        print ("Sorry record not found")
f.close()
    
