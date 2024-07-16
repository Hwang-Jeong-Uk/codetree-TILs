s, q= input().split()
q=int(q)

for i in range(q):
    cont=int(input())
    if cont == 1:
        s=s[1:]+s[0]
    elif cont == 2 :
        s=s[-1]+s[:-1]
    elif cont == 3 :
        s=s[::-1]
    print(s)