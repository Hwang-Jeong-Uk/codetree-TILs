string1,string2=input().split()

if len(string1)==len(string2):
    print('same')
elif len(string1) > len(string2):
    print(string1,end=" ")
    print(len(string1))
else:
    print(string2,end=" ")
    print(len(string2))