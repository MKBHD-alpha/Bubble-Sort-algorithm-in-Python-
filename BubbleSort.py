a= [int(a) for a in input("Enter multiple value: ").split()]
a= [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10]
count=0
for i in range(len(a)):
    for j in range(1,len(a)):
        if a[j-1] > a[j]:
            count+=1
            a[j-1],a[j]= a[j], a[j-1]
print(a)
print(f"The Total No. of times it was Swapped is {count}")
