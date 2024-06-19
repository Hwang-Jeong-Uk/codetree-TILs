sum_val=0
cnt=0
prod=1

while True:
    n=int(input())
    if n//10!=2:
        break
    else:
        sum_val += n
        cnt += 1
print(f"{sum_val/cnt:.2f}")