N=input()
length=len(N)

cnt=0
cntt=0
for i in range(length-1):
    if N[i] == 'e' and N[i+1] == 'e':
        cnt += 1
    elif N[i] == 'e' and N[i+1] == 'b':
        cntt += 1
    
print(cnt,end=" ")
print(cntt)