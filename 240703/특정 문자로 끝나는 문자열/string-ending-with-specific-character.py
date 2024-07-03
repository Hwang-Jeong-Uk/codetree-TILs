arr=[input() for _ in range(10)]
alp=input()
cnt=0
for i in arr:
    if alp == i[-1]:
        print(i) 
        cnt+=1
if cnt == 0:
    print('None')