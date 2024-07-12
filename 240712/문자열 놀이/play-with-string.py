s,q=input().split()
q=int(q)
s=list(s)
ss=""
sss=""
for i in range(q):
    S=list(input().split())
    S_0=int(S[0])
    if S_0==1:
        ss=s[int(S[2])-1]
        sss=s[int(S[1])-1]
        s[int(S[2])-1]=sss
        s[int(S[1])-1]=ss
        for k in range(len(s)):
            print(s[k],end="")
    elif S_0==2:
        for j in range(len(s)):
            if s[j] == S[1]:
                s[j] = S[2]
        for k in range(len(s)):
            print(s[k],end="")
    print()