n=int(input())
arr=list(map(int,input().split()))
arrt=[]

arrt=[i for i in arr if i%2==0]
for j in arrt:
    print(j,end=" ")