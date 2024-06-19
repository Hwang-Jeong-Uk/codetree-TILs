N=int(input())
x=0

while N != 1:
    if N%2 ==0:
        x +=1
        N=N//2
print(x)