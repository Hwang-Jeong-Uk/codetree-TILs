arr=list(map(int,input().split()))
arrt=[]

for i in range(len(arr)):
    if arr[i] %3 ==0:
        print(arr[i-1])
        break