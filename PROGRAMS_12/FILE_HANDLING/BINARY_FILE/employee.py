import pickle
e1=[1,"Aman",5000]
e2=[2,"Bipin",9000]
e3=[4,"Dinakar",9900]
f=open("employee.dat","wb")
pickle.dump(e1,f)
pickle.dump(e2,f)
pickle.dump(e3,f)
f.close()


