n=int(input())
cnt=0
arrt=[]

for i in range(0,100):
    
    arrt.append(n*(i+1))

    if arrt[i]%5==0:
        cnt +=1
        
    print(arrt[i],end=" ")
    if cnt==2:
        break