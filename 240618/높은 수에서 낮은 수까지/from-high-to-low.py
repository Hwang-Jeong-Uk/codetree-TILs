a,b=input().split()
a=int(a)
b=int(b)

if a>=b:
    for a in range(a,b-1,-1):
        print(a,end=" ")
else:
    for b in range(b,a-1,-1):
        print(b,end=" ")