import csv
ans='y'
with open("employee.csv",mode='r')as f:
    myreader=csv.reader(f,delimiter=',')
    while ans.lower()=='y':
        found=False
        e=int(input("Enter the employee number to search"))
        for row in myreader:
            if len(row)!=0:
                if int(row[0])==e:
                    print('Name=',row[1])
                    print('Salary=',row[2])
                    found=True
                    break
        if not found:
            print("NO RECORD FOUND")
        ans=input("do yo want to search more?(y/n)") 


                
           
