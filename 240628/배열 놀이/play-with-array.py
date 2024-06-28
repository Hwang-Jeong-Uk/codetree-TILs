n,q=map(int,input().split())

arr=list(map(int,input().split()))
arrtt=[]
cnt = 0

for _ in range(q):
    arrt= list(map(int,input().split()))
    if arrt[0] == 1:
        print(arr[arrt[1]-1])

    elif arrt[0] == 2:
        if arrt[1] in arr:
            c=arr.index(arrt[1])+1
            print(c)
        elif arrt[1] not in arr:
            print(0)

    elif arrt[0] == 3:
        for k in range(arrt[1],arrt[2]+1):
            print(arr[k-1],end=" ")