c,n=input().split()
n=int(n)
i=1
if c == 'A':
    for i in range(1,n+1):
        print(i,end=" ")
elif c == 'D':
    for i in range(n,1-1,-1):
        print(i,end=" ")