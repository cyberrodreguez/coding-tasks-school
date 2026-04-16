def maxin():
    L=[]
    n=int(input("Please enter element length in list "))
    for i in range(1,n+1):
        a=int(input("Please enter the Value of %d Element : " %i))
        L.append(a)
    print("The Smallest Element in this List is : ", min(L))
    print("The Largest Element in this List is : ", max(L))
