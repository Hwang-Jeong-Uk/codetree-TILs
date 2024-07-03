a=input()
b=input()
c=input()

lena=len(a)
lenb=len(b)
lenc=len(c)
arr=[lena,lenb,lenc]
max_len=max(arr)
min_len=min(arr)
print(max_len-min_len)