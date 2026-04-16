myfile=open("yo.txt","r")
str1=" "
org_size=0
rem_size=0
while str1:
    str1=myfile.readline()
    org_size=org_size+len(str1)
    rem_size=rem_size+len(str1.strip())
print("size of the file after removing all EOL characters and blank spaces",rem_size)
print("total size of the file",org_size)

