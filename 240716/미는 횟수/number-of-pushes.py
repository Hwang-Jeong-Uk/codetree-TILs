A=input()
B=input()
num=0
while True:
    A=A[-1]+A[:-1]
    num+=1
    if A==B:
        break
print(num)