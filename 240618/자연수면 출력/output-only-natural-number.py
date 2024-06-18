a,b=input().split()
a=int(a)
b=int(b)
c=a%1
if c==0:
    for _ in range(b):
        print(a,end="")