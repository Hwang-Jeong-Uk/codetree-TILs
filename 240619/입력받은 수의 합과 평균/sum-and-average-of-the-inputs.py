n=int(input())
sum_val=0
cnt=0

for i in range(n):
    nn=int(input())
    sum_val += nn
    cnt +=1
print(sum_val,f"{sum_val/cnt:.1f}")