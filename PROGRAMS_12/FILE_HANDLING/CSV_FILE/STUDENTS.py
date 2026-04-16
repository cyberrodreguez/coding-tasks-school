#*************************************WRITE***************************************
import csv
fields=['NAME','CLASS','YEAR']
rows=[['Rohith','XII','2000'],
        ['Arif','XII','2003'],
        ['Deep','XII','2004']]
file=open("students.csv","w",newline='')
csv_w=csv.writer(file,delimiter=',')
csv_w.writerow(fields)
for i in rows:
    csv_w.writerow(i)
print("file created")
file.close()
#*************************************READ*************************************
def read():
    import csv
    f=open("students.csv","r")
    k=csv.reader(f)
    for i in k:
        print(i)
    f.close()    
#*************************************SEARCH*************************************
def search():
    import csv
    f=open("students.csv","r")
    csv_reader=csv.reader(f)
    name=input("Enter Name to search")
    for row in csv_reader:
        if row[0].lower()==name:
           print(row)
    f.close()
