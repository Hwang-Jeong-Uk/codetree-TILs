N=int(input())
arr= list(map(int,input().split()))
d=1
while d != 0:
    c=arr.index(max(arr))+1
    print(c,end=" ")
    d=c-1
    arr=arr[0:d]