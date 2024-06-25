a,b=input().split()
a=int(a)
b=int(b)

for i in range(1,5):
    for j in range(b,a-1,-1):
        print(f"{j} * {2*i} = {2*i*j}", end=" ")
        if j > a:
            print("/",end=" ")
    print()