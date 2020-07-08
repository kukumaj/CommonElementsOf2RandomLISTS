import random
q=random.randint(1,50)
print(str(q)+' numbers will be drawn to each A and B lists but they will be sorted  and duplicates will be removed'+'\n')
print ()
l1=[random.randint(1,30) for i in range(0,q)]
l2=[random.randint(1,30) for i in range(0,q)]
print ('list A before sorting and removing duplicates')
print ()
print(l1)
print ()
print ('list B before sorting and removing duplicates')
print ()
print(l2)
print ()
A=sorted(list(set(l1)))
B=sorted(list(set(l2)))
def wspel(A,B):
    i1=0
    i2=0
    wyn=[]
    while i1<len(A) and i2<len(B):
        if A[i1]==B[i2]:
            wyn.append(A[i1])
            i1+=1
            i2+=1
        elif A[i1]>B[i2]:
            i2+=1
        else:
            i1+=1
    return wyn
#A=list(range(0,100))
#B=list(range(0,100))
print ('Lists A and B after sorting and removing duplicates')


print ()
print ('list A')

print(A)
print ()
print ('list B')
print (B)

print ()
print ('common elments are-->>>')
print(wspel(A,B))
