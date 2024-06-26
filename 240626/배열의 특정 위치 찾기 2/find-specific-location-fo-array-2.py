arr=list(map(int,input().split()))
sum_val=0
sum_vall=0

for i in range(len(arr)):
    if i%2==0:
        sum_val += arr[i]
    else:
        sum_vall += arr[i]

if sum_val >= sum_vall:
    print(sum_val-sum_vall)
else:
    print(sum_vall-sum_val)