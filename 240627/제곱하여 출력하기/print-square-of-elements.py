n = int(input())

arr= list(map(int,input().split()))

arrt=[i**2 for i in arr]
for j in range(n):
    print(f"{arrt[j]}",end=" ")