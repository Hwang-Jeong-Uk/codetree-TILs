arr=list(map(int,input().split()))
arrt=[]

for i in arr:
    if i == 0:
        break
    arrt.append(i)

sum_val=sum(arrt)
mean_val=round(sum(arrt)/len(arrt),1)
print(sum_val,end=" ")
print(mean_val)