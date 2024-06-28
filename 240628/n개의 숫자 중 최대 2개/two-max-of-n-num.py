N=int(input())
arr=list(map(int,input().split()))
arrt=[]

max_val=arr[0]
for _ in range(N):
    for i in range(N-1):
        if arr[i]<=arr[i+1]:
            a=arr[i]
            arr[i]=arr[i+1]
            arr[i+1]=a
        
for k in range(2):
    print(arr[k],end=" ")