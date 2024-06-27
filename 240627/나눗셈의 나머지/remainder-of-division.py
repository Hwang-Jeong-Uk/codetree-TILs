arr= list(map(int,input().split()))
a,b=arr[0],arr[1]
count=[0]*10
arrt=[]
while True:
    c=a%b
    count[c] +=1
    a=a//b
    if a<=1:
        break
arrt=[i**2 for i in count]
print(sum(arrt))