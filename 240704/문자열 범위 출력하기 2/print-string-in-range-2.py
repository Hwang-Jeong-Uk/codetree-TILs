string=input()
num=int(input())

if len(string) >= num:
    for i in range(num):
        print(string[len(string)-i-1],end="")
else:
    print(string[::-1])