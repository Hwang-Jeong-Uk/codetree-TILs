arr=[input() for _ in range(10)]
alp=input()

for i in arr:
    if alp == i[-1]:
        print(i) 
    else:
        print('None')