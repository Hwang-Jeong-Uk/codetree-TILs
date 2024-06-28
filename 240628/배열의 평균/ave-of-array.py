arr_2d=[list(input().split()) for _ in range(2)]
ga_=[0]*2
se_=[0]*4

for i in range(2):
    
    for j in range(4):
        ga_[i] += int(arr_2d[i][j])
        se_[j] += int(arr_2d[i][j])
ga_sum=sum(ga_)
se_sum=sum(se_)
sum_sum=ga_sum+se_sum
for k in range(2):
    print(f"{ga_[k]/4:.1f}",end=" ")
print()
for h in range(4):
    print(f"{se_[h]/2:.1f}",end=" ")
print()
print(f"{sum_sum/16:.1f}")