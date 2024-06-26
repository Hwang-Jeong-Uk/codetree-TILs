arr=list(map(int,input().split()))
arrt=[]

for i in arr:
    if i ==0:
        break
    arrt.append(i)

rev_arrt=arrt[::-1]
for i in rev_arrt:
    print(i,end=" ")