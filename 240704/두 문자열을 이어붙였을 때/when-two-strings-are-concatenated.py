A=input()
B=input()

answer="true"

AB=A+B
BA=B+A

for i in range(len(AB)):
    if AB[i] != BA[i]:
        answer='false'
        break

print(answer)