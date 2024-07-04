s = input()
# print('Yes' if 'ee' in s else 'No',end =" ")
# print('Yes' if 'ab' in s else 'No')
answer='No'
ansswer='No'
for i in range(len(s)-1):
    if s[i] == 'e' and s[i+1] == 'e':
        answer='Yes'
    elif s[i] == 'a' and s[i+1] == 'b':
        ansswer='Yes'

print(answer,end=" ")
print(ansswer)