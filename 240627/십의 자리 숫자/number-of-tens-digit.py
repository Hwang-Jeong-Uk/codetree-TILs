arr= list(map(int,input().split()))
count=[0]*(len(arr)+1)

for i in range(len(arr)):
    if arr[i] == 0:
        for k in range(1,10):
            print(f"{k} - {count[k]}")
        break
    ten=arr[i]//10
    count[ten] += 1