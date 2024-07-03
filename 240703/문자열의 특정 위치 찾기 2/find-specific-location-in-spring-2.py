a=input()
arr=["apple", "banana", "grape", "blueberry", "orange"]
cnt=0
for i in arr:

    if a == i[2] or a == i[3]:
        print(i)
        cnt +=1
print(cnt)