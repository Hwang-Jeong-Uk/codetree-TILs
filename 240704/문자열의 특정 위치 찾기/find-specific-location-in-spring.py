arr=input().split()
A=arr[0]
B=arr[1]

length=len(A)
start_idx='No'

for i in range(length-len(B)+1):
    if A[i] == B:
        start_idx=i
        break
print(start_idx)