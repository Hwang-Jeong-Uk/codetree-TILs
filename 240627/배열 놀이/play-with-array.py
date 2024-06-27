n,q=input().split()
n,q=int(n),int(q)

arr=list(map(int,input().split()))
arrtt=[]
for i in range(q):
    arrt=[]
    arrt=list(map(int,input().split()))
    if arrt[0]==1:
        print(arr[arrt[1]-1])
        continue
    elif arrt[0]==2:
        for j in range(len(arr)):
            if arr[j]==arrt[1]:
                print(j+1)
        continue
    else:
        start= arrt[1]-1
        end =arrt[2]
        arrtt=arr[start:end]
        for k in arrtt:
            print(k,end=" ")