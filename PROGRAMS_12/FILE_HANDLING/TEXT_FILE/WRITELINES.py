file=open("new.txt","w")
list1=[]
for i in range(5):
    name =input("enter name of the student")
    list1.append(name +'\n')
file.writelines(list1)
file.close()
