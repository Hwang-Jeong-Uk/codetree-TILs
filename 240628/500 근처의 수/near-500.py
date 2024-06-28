arr=list(map(int,input().split()))
arrt=[]
arrtt=[]
for i in arr:
    if i < 500:
        arrt.append(i)
    elif i >500:
        arrtt.append(i)

print(max(arrt),end=" ")
print(min(arrtt))