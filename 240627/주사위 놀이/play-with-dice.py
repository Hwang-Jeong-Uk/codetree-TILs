arr= list(map(int,input().split()))
arrt=[0]*7

for i in arr:
    arrt[i] +=1
for j in range(1,7):
    print(f"{j} - {arrt[j]}")