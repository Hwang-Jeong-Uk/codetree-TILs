n=int(input())
prod=1
cnt=0
for i in range(1,11):
    prod *= i
    cnt=i
    if prod >= n:
        break
print(cnt)