n,q=input().split()
n,q=int(n),int(q)

arr=list(map(int,input().split()))
arrtt=[]
cnt = 0
count=[0]
for i in range(q):
    arrt=[]
    arrt=list(map(int,input().split()))
    if arrt[0]==1:
        print(arr[arrt[1]-1])
        continue
    elif arrt[0]==2:
        for j in range(len(arr)):
            if arr[j]==arrt[1]:
                cnt +=1
                count.append(arr[j])
                if cnt>=2:
                    print(count[1])
                elif cnt==1:
                    print(j+1)
                else:
                    print(0)
                
        continue
    else:
        start= arrt[1]-1
        end =arrt[2]
        arrtt=arr[start:end]
        for k in arrtt:
            print(k,end=" ")