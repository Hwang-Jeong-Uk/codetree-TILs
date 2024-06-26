arr=list(map(int,input().split()))
sum_val=0
sum_vall=0
cnt=0
arrt=[]

for i in range(len(arr)):
    if i%2==1:
        sum_val += arr[i]
    if (i+1)%3==0:
        sum_vall += arr[i]
        cnt +=1

print(sum_val,end=" ")
print(round(sum_vall/cnt,1))