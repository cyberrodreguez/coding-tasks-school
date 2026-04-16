import csv
k='y'
s=input("Do you want to add an employee?(y/n)")
if s.lower()==k:
    with open("employee.csv",mode="a",newline='')as f:
        mywriter=csv.writer(f,delimiter=',')
        ans='y'
        while ans.lower()=='y':
            eno=int(input("Enter employee number"))
            name=input("Enter employee name")
            salary=int(input("Enter employee salary"))
            mywriter.writerow([eno,name,salary])
            print("////////////////////DATA SAVED////////////////////")
            ans=input("Add more?(y/n)")



'''if found==False:
                print("NO RECORD FOUND")'''




'''k='y'
s=input("Do you want to get full details of the employees?(y/n)")
if s.lower()==k:
    with open("employee.csv","r")as f:
        k=csv.reader(f)
        print("////////////////////DETAILS//////////////////")
        for i in k:
            print(i)'''



