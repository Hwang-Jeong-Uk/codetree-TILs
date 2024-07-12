s=input()
s=list(s)
s_0=s[0]
s_1=s[1]
for i in range(len(s)):
    
    if s[i]==s_1:
        s[i]=s_0
    
for k in range(len(s)):
    print(s[k],end="")