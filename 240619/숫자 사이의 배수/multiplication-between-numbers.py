a,b=input().split()
a=int(a)
b=int(b)
sum_val=0
get=0
for i in range(a,b+1):
    if i%5==0 or i%7==0:
        sum_val += i
        get += 1
print(sum_val,f"{sum_val/get:.1f}")