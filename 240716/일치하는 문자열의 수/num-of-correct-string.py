num,s=input().split()
num=int(num)

count=0

for i in range(num):
    ss=input()
    if ss == s:
        count +=1

print(count)