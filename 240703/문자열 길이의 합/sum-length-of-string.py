n=int(input())
arr=[input() for _ in range(n)]
cnt=0
cntt=0

for i in arr:
    cnt += len(i)
    if 'a' == i[0]:
        cntt += 1
print(cnt,end=" ")
print(cntt)