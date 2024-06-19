sat=True

for i in range(5):
    n=int(input())
    if n%3 != 0 :
        sat=False

if sat == False:
    print(0)
else:
    print(1)