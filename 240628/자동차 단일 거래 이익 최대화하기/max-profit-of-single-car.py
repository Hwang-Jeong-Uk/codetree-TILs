n=int(input())
arr=list(map(int,input().split()))

# year + 1이 진짜 년도인걸 기억

arrt=[]
max_price=0

for year, price in enumerate(arr):
    arrt=arr[year:]    
        
    for prices in arrt:
        sub_price = (prices-price)
        if sub_price > max_price:
            max_price = sub_price
         
    


print(max_price)