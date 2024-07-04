n=int(input())
arr=input().split()

N="".join(arr)
cnt=0
for i in range(len(N)):
    
    if cnt==5:
        print()
        cnt=0
    print(N[i],end="")
    cnt+=1