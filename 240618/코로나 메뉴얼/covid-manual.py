p1,d1=input().split()
p2,d2=input().split()
p3,d3=input().split()

d1=int(d1)
d2=int(d2)
d3=int(d3)

A=0
B=0
C=0
D=0

if p1 == 'Y' :
    if d1 >= 37 :
        A += 1
    else:
        C += 1
else:
    if d1 >= 37 :
        B += 1
    else:
        D += 1

if p2 == 'Y' :
    if d2 >= 37 :
        A += 1
    else:
        C += 1
else:
    if d2 >= 37 :
        B += 1
    else:
        D += 1

if p3 == 'Y' :
    if d3 >= 37 :
        A += 1
    else:
        C += 1
else:
    if d3 >= 37 :
        B += 1
    else:
        D += 1

if A>=2:
    print('E')
else:
    print('N')