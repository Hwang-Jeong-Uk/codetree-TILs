A=list(input())
B=list(input())

while True:
    idx=-1
    for i in range(len(A)-len(B)+1):
        it_same=True

        for j in range(len(B)):
            if A[i+j] != B[j]:
                it_same=False
                break
        if it_same:
            idx = i
            break
    if idx == -1:
        break
    
    A=A[:idx]+B[idx+len(B):]

A="".join(A)
print(A)