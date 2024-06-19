n=int(input())

sum_val=0
for i in range(1,(n)//2):
    if n%i==0:
        sum_val += n//i+i

sum_val=sum_val-n
if sum_val==n:
    print('P')
else:
    print('N')