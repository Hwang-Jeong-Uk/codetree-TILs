n=int(input())
arr=list(map(int, input().split()))
arrt=[]
for i in arr:
    if i%2==0:
        arrt.append(i)
arrt=arrt[::-1]
for j in arrt:
    print(j,end=" ")