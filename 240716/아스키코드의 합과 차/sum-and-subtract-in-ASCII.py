a,b=input().split()

add_ab=ord(a)+ord(b)
if ord(a)>ord(b):
    sub_ab=ord(a)-ord(b)
elif ord(a)<=ord(b):
    sub_ab=ord(b)-ord(a)

print(add_ab,end=" ")
print(sub_ab)