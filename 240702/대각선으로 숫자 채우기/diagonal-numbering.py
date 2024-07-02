n,m=tuple(map(int,input().split()))

arr=[[0 for _ in range(m)] for _ in range(n)]
cnt=1

for start_col in range(m):
    curr_row = 0
    curr_col = start_col

    while 0<= curr_col and curr_row < n:
        arr[curr_row][curr_col]=cnt

        curr_row += 1
        curr_col -= 1
        cnt +=1
    
for start_row in range(1,n):
    curr_col = m-1
    curr_row = start_row

    while curr_row < n and curr_col <m:
        arr[curr_row][curr_col]=cnt

        curr_row += 1
        curr_col -= 1
        cnt+=1
    
for i in range(n):
    for j in range(m):
        print(arr[i][j],end=" ")
    print()