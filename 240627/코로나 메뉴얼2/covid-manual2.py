cnt=0
count=[0]*4
for i in range(3):
    a,b=input().split()
    b=int(b)

    if a == 'Y': 
        if b>=37:
            
            cnt +=1
            count[0] += 1
        else:
            
            count[2] += 1
    else:
        if b>=37:
            
            count[1] += 1
        else:
            
            count[3] += 1
for j in range(4):
    print(f"{count[j]}",end=" ")
if cnt >=2:
    print('E')