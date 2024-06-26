arr=list(map(int, input().split()))
arrr=[]
sum_val=0
cnt=0

for i in arr:
    if arr[cnt] >=250:
        break
    arrr.append(i)
    sum_val += arrr[cnt]
    cnt += 1

print(sum_val,end=" ")
print(sum_val/len(arrr))