n=int(input())
sum_val=0
for i in range(n):
    aa=int(input())
    sum_val += aa

s= str(sum_val)
s=s[1:]+s[0]
print(s)