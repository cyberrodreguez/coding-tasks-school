import csv
f=open("employee.csv","r")
csv_reader=csv.reader(f)
ans='y'
while ans=='y':
    name=input("Enter Name to search")
    for row in csv_reader:
        if row[0].lower()==name:
            print(row)
f.close()
