n=int(input())
cnt=0
cnt_nt=0
for i in range(1,n+1):
    if i%2==0 or i%3==0 or i%5==0:
        cnt +=1
        continue
    cnt_nt +=1
print(cnt_nt)