arr = list(map(int,input().split()))
arrt=[]
for i in arr:
    if i == 999 or i == -999:
        break
    arrt.append(i)
print(max(arrt),end=" ")
print(min(arrt))