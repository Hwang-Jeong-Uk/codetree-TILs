A=list(input())
B=list(input())
AA=[]
BB=[]
for i in range(len(A)):
    if A[i].isdigit():
        AA.append(A[i])

for j in range(len(B)):
    if B[j].isdigit():
        BB.append(B[j])

A="".join(AA)
B="".join(BB)

A,B=int(A),int(B)
add_AB=A+B
print(add_AB)