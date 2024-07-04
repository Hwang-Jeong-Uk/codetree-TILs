n=int(input())
arr=[input() for _ in range(n)]

# N="".join(arr)
# print(N)

NN=""
for i in range(len(arr)):
    NN += (arr[i])
    
print(NN)