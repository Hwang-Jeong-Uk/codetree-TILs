a,b,c= input().split()
a=int(a)
b=int(b)
c=int(c)

if (a>b>c)or(c>b>a):
    print(b)
elif (a>c>b)or(b>c>a):
    print(c)
else:
    print(a)