n=int(input())
cnt=0
for i in range(n):
    arr=list(map(int,input().split()))
    if round(sum(arr)/len(arr),1)>=60:
        print('pass')
        cnt +=1
    else:
        print('fail')
print(cnt)