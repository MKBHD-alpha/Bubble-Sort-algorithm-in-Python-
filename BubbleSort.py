n1=int(input("Enter Number 1:- "))
n2=int(input("Enter Number 2:- "))
n3=int(input("Enter Number 3:- "))
n4=int(input("Enter Number 4:- "))
n5=int(input("Enter Number 5:- "))
n6=int(input("Enter Number 6:- "))
n7=int(input("Enter Number 7:- "))
n8=int(input("Enter Number 8:- "))
n9=int(input("Enter Number 9:- "))
n10=int(input("Enter Number 10:- "))

a= [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10]
count=0
for i in range(len(a)):
    for j in range(1,len(a)):
        if a[j-1] > a[j]:
            count+=1
            a[j-1],a[j]= a[j], a[j-1]
print(a)
print(f"The Total No. of times it was Swapped is {count}")
