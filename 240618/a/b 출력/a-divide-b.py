# 입력을 받고, 정수로 변환
a, b = input().split()
a = int(a)
b = int(b)

# 결과를 저장할 리스트 초기화
c = [0] * 20
print(f"{a//b}.",end="")

# 20번 반복하며 a의 거듭제곱을 계산하여 b로 나눈 몫을 리스트에 저장
for i in range(20):
    a=a%b*10
    print(a//b,end="")