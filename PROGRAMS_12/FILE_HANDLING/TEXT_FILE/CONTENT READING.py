file=open("yo.txt","r")
print(file.read())
file.close()
print("1111111111111111111111111111111111111111111111")
file=open("yo.txt","r")
print(file.readlines())
file.close()
print("1111111111111111111111111111111111111111111111")
file=open("yo.txt","r")
a=file.readline()
while a:
    print(a)
    a=file.readline()
file.close()
print("1111111111111111111111111111111111111111111111")
myfile = open("yo.txt", "r")
while myfile:
    line  = myfile.readline()
    print(line)
    if line == "":
        break
myfile.close() 
print("1111111111111111111111111111111111111111111111")
myfile = open("yo.txt", "r")
for line in myfile:
    print(line)
myfile.close()   
