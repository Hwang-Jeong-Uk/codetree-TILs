n1,n2=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
count=[]
cnt=0

for o,k in enumerate(B):
    if k in A:
        count.append(A.index(k))
        
    else:
        pass
for i in range(len(count)-1):
    cnt += (count[i+1]-count[i])
    
if cnt == (len(count)-1):
    print('Yes')
else:
    print('No')