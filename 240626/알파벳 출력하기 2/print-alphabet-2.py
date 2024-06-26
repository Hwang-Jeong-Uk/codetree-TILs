N=int(input())
cnt='A'
for i in range(N):
    for k in range(i):
            print(" ",end=" ")
    for j in range(N-i):
        
        print(cnt,end=" ")
        if cnt=='Z':
            cnt='A'
        else:
            cnt = chr(ord(cnt)+1)
    print()