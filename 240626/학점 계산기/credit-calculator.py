n = int(input())
arr = list(map(float, input().split()))

sum_val=sum(arr)
print(f'{sum_val/len(arr):.1f}')

mean_=round(sum_val/len(arr),1)

if mean_>=4.0:
    print('Perfect')
elif mean_>=3.0:
    print('Good')
else:
    print('Poor')