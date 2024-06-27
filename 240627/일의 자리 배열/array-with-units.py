a,b=map(int,input().split())
arr=[0,a,b]

for i in range(3,11):
    arr.append((arr[-1]+arr[-2])%10)

for j in range(1,11):
    print(arr[j],end=" ")