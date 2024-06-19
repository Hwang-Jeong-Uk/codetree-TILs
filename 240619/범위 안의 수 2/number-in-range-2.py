cnt=0
sum_val=0
for _ in range(10):
    n=int(input())
    if n>=10 and n<=200:
        cnt += 1
        sum_val += n
print(sum_val,f"{sum_val/cnt:.1f}")