A=input()
B=input()
num=0
while True:
    A=A[-1]+A[:-1]
    num+=1
    if A==B:
        idx=1
        break
    if num==len(A):
        idx=-1
        break
if idx == 1:
    print(num)
else:
    print(idx)