myfile=open("students.txt","w")
for i in range(3):
    name=input("enter a name")
    myfile.write(name)
    myfile.write('\n')
myfile.close()
print("Data Saved Successfully")
