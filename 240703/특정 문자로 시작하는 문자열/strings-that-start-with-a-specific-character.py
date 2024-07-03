n=int(input())
arr=[input() for _ in range(n)]
alp=input()
cnt=0
sum_val=0

for i in arr:
    if alp == i[0]:
        cnt += 1
        sum_val += len(i)
    
print(cnt,end=" ")
print(f"{sum_val/cnt:.2f}")