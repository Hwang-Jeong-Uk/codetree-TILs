arr=list(map(int,input().split()))
arrt=[]

for i in arr:
    if i%2 == 1:
        print(i+3,end=" ")
    elif i%2==0 and i !=0:
        print(i//2,end=" ")
    elif i==0:
        break