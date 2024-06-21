n=int(input())

for i in range(n):
    for j in range(n):
        for k in range(n):
            print("*",end="")
        print(end=" ")
    print()
    n -=1