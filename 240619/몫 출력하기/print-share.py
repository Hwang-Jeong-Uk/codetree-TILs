cnt=0
while True:
    n=int(input())
    if n%2!=0:
        continue
    elif n%2==0:
        c=n//2
        print(c)
        cnt += 1
    if cnt == 3:
        break