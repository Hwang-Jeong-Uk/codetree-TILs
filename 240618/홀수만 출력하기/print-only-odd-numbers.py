N=input()
i=0
while i<len(N) :
    e=int(N[i])
    if e%2 != 0 and e%3==0:
        print(e)
    else:
        pass
    i += 1