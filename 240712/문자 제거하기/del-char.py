s=input()
arr=list(s)

for _ in range(len(arr)):
    q=int(input())

    if q > len(arr):
        arr.pop(-1)
    else:
        arr.pop(q)
    s="".join(arr)
    print(s)
    arr=list(s)
    if len(arr) == 1:
        break