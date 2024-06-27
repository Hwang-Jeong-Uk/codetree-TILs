n=input()
LEBROS=['L','E','B','R','O','S']

for i,char in enumerate(LEBROS):
    if char == n:
        print(i)

if n not in LEBROS:
    print('None')