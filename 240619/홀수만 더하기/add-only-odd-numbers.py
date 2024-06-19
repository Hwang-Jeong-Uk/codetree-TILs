n=int(input())
sum_val=0
for i in range(n):
    v=int(input())
    if v%2!=0 and v%3==0:
            sum_val += v
print(sum_val)