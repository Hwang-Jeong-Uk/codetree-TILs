a,b,c= input().split()
a=int(a)
b=int(b)
c=int(c)

if a>b:
    if b>c:
        print(b)
    elif c>a:
        print(a)
if a>c:
    if c>b:
        print(c)
    elif b>a:
        print(a)
if c>b:
    if b>a:
        print(b)
    elif a>c:
        print(c)