import pickle
emp1={"empno":123,"name":'Arif',"age":12}
emp2={"empno":124,"name":'Adhoith',"age":12}
emp3={"empno":125,"name":'Amrith',"age":12}
empfile=open("emp.dat","wb")
pickle.dump(emp1,empfile)
pickle.dump(emp2,empfile)
pickle.dump(emp3,empfile)
print("successfully written")
empfile.close()
