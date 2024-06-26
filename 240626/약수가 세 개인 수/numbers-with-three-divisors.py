start,end=input().split()
start=int(start)
end=int(end)
cntt=0

for i in range(start,end+1):
    cnt=0
    for j in range(1,i+1):
        if i%j==0:
            cnt += 1
    if cnt == 3:
        cntt +=1
print(cntt)