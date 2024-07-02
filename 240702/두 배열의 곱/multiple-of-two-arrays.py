arr=[[0 for _ in range(3)] for _ in range(3)]
arrt=[[0 for _ in range(3)] for _ in range(3)]
arrr=[[0 for _ in range(3)] for _ in range(3)]


for i in range(3):
    arr[i]=list(map(int,input().split()))

space=input()

for j in range(3):
    arrt[j]=list(map(int,input().split()))

for i in range(3):
    for j in range(3):
        arrr[i][j]=arr[i][j]*arrt[i][j]
        print(arrr[i][j],end=" ")
    print()