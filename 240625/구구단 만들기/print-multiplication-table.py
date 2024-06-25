a,b=input().split()
a=int(a)
b=int(b)
cnt=1
for i in range(1,10):
    for j in range(b,a-1,-2):
        print(f"{j} * {i} = {j*i}",end=" ")
        if cnt<((b-a)//2+1) :
            print("/",end=" ")
            cnt+=1
        else:
            cnt=1
    print()