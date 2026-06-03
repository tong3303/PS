import sys

n = 4

raw = [i for i in range(1, n+1)]
print(raw)

while True:
    # 1. 꺾이는 부분 찾기
    for i in range(n-1, 0, -1):  # 3, 2, 1
        if raw[i] > raw[i-1]:
            break
    else:
        break

    # 2. 최솟값 찾기
    key = raw[i-1]
    for j in range(n-1, i-1, -1):
        if raw[j] > key:
            break

    # 3. 둘을 바꿔주기
    raw[i-1], raw[j] = raw[j], raw[i-1]

    # 4. raw[i] 부분 이후 정렬하기
    raw[i:] = reversed(raw[i:])
    print(raw)