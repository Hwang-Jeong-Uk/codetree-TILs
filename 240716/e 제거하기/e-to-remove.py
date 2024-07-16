s=input()
s=list(s)
for i in range(len(s)):
    if s[i] =='e':
        s.pop(i)
        s="".join(s)
        break
print(s)