N=int(input())
arr=list(map(int,input().split()))
arrt=[]
idx=-1

for i in arr:
    if idx<i:
        count = 0
        for elem in arr:
            if  elem == i:
                count += 1
        if count == 1:
            idx = i

print(idx)