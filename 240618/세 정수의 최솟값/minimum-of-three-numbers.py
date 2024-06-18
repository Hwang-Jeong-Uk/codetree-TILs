a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)

if a<=b and a<=c:
    print(f"{a}")
elif b<=a and b<=c:
    print(b)
else: 
    print(c)