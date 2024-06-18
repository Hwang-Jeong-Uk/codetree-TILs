n=int(input())
cnt=0
cntt=0
cnttt=0
for i in range(1,n+1):
    if i%12==0:
        cnt +=1
    elif i%3==0:
        cntt +=1
    elif i%2==0:
        cnttt +=1

print(cnttt,cntt,cnt)