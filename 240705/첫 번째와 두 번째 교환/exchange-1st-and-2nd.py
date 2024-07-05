A=input()
a=A[0]
b=A[1]
B=""
for i in range(len(A)):
    if A[i] == a:
        B += b
    elif A[i] == b:
        B += a
    else:
        B += A[i]

print(B)