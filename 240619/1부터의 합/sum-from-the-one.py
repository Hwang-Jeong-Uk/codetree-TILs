n=int(input())
sum_val=0
cnt=0
for i in range(1,101):
    sum_val += i
    cnt=i
    if sum_val >=n:
        break
print(cnt)