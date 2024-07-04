string=input()
num=int(input())

for i in range(num):
    print(string[len(string)-i-1],end="")