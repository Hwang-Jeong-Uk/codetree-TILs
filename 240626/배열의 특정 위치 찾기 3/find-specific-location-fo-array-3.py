arr=list(map(int,input().split()))
arrt=[]

for i in arr:
    if i == 0:
        break
    arrt.append(i)
sum_val=sum(arrt[-3:])
print(sum_val)