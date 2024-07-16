s=input()
s=list(s)
for i in s:
    cont=i.isalpha()
    if cont:
        if ord(i)>=ord('a'):
            num=ord(i)-ord('a')+ord('A')
            stri=chr(num)
            print(stri,end="")
        else:
            print(i,end="")