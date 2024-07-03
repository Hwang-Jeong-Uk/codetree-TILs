a=input()
b=input()
arra=[0 for _ in range(len(a))]
arrb=[0 for _ in range(len(b))]

for i in range(len(a)):
    if " " in a[i]:
        continue
    else:
        print(a[i],end="")
for i in range(len(b)):
    if " " in b[i]:
        continue
    else:
        print(b[i],end="")