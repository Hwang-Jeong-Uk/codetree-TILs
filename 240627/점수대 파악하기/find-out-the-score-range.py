arr=list(map(int,input().split()))
count=[0]*(11)
cnt=0
while True:
    if arr[cnt]==0:
        for j in range(100,0,-10):
            print(f"{j} - {count[j//10]}")
        break
    cntt=arr[cnt]//10
    count[cntt] +=1
    
    cnt += 1