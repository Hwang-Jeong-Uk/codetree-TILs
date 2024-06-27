n=input()
LEBROS=['L','E','B','R','O','S']

for i,char in enumerate(LEBROS):
    if char == n:
        print(i)

if 'L' not in LEBROS:
    print('None')