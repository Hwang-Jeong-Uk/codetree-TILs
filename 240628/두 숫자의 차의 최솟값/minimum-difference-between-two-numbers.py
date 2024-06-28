n=int(input())
arr= list(map(int,input().split()))

vs_num=arr[-1]
for num in arr:
    for nums in arr:
        sub_num=nums-num
        if sub_num < vs_num and sub_num > 0:
            vs_num = sub_num
print(vs_num)