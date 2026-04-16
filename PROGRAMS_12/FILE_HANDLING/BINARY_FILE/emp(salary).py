import pickle
def recshow():
    emp=[]
    found=False
    f=open('employee.dat','rb')
    while True:
        try:
            emp=pickle.load(f)
        except EOFError:
            break
    print("EMP_NO", "/t", "EMP_NAME", "/t", "EMP_SALARY")
    print("*********** **********************************************")
    for e in emp:
        if (e[2]>7000):
            print(e[0] ,"/t" ,e[1],"/t" ,e[2])
            found=True
        else:
            print("No records found")
