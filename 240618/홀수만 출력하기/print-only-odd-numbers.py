N = int(input())

i = 0
# N개의 정수를 순서대로 입력받습니다.
while i < N:
    number = int(input())
    # 입력된 수가 홀수이면서 3의 배수인지 확인합니다.
    if number % 2 != 0 and number % 3 == 0:
        print(number)
    i += 1