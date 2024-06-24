n=int(input())
cnt=1
cntt=n
for i in range(2*n):
    if i%2==0:
        for j in range(cnt):
            print("*",end=" ")
        cnt +=1
    else:
        for k in range(cntt):
            print("*",end=" ")
        cntt -=1    
    print()