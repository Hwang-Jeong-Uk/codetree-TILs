a,b=map(int,input().split())
ab=a+b
ab=str(ab)
ab=list(ab)
count=0
for i in ab:
    if i == '1':
        count +=1
print(count)