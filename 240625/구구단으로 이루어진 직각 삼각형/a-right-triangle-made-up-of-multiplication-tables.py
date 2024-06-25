n=int(input())

for i in range(1,n+1):
    for j in range(n-i+1):
        if (i+j+1)==6:
            print(f"{i} * {j+1} = {i*(j+1)}",end="\n")
        else:
            print(f"{i} * {j+1} = {i*(j+1)}",end=" ")
            print("/",end=" ")