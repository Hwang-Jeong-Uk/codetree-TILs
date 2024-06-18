a,b=input().split()
a=int(a)
b=int(b)
c=a%1
if c==0 and a>0:
    for _ in range(b):
        print(a,end="")
elif a<=0:
    print(0)