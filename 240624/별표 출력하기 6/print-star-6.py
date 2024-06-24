n=int(input())

for i in range(n-1,-1,-1):
    for g in range(n-i-1):
        print(" ",end=" ")

    for j in range(2*i+1):
        print("*",end=" ")
    print()

for i in range(1,n):
    for g in range(n-1-i):
        print(" ",end=" ")

    for j in range(2*i+1):
        print("*",end=" ")
    print()