n=int(input())
k=0
for i in range(n):
    k=i+1
    for j in range(n):
        print(k,end=" ")
        k +=n
    print()