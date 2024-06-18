n=int(input())
i=1
while n>=i:
    if i%3==0 or (i//10%3==0 and i>=10) or (i%10%3==0 and i>=10) :
        print(0, end=" ")
    else:
        print(i,end=" ")
    i += 1