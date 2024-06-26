arr=list(map(int,input().split()))
arrt=[]

for i in arr:
    if i==0:
        break
    if i%2==0:
        arrt.append(i)
print(len(arrt),end=" ")
print(sum(arrt))