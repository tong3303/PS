# 100 * (100,000의 R | D를 처리) 배열의 길이 = 600,000 < 300,000,000

import sys
from collections import deque

input = sys.stdin.readline
instructionAmount = int(input())

for i in range(instructionAmount):
    instruction = input().strip()
    arrayLen = int(input())

    # 빈 배열일 때는 상관없지만, 빈 배열일 때 D를 사용하면 에러임.
    # 빈 배열일 때 error가 출력하도록 코드를 짜서 틀림.
    # try:
    #     array = deque(map(int, input().strip().strip("[]").split(",")))
    # except ValueError:
    #     print("error")
    #     continue
    
    # 수정한 코드
    arrayString = input().strip()
    if arrayString == "[]":
        array = deque()
    else:
        array = deque(arrayString[1:-1].split(','))

    isFrontPop = True
    for j in instruction:
        if array and j == "D":
            if isFrontPop: array.popleft()
            else: array.pop()

        elif j == "R":
            isFrontPop = not isFrontPop

        else:
            print("error")
            break

    else:
        if not isFrontPop:
            array.reverse()
        printArray = list(map(str, array))
        print("[", end="")
        print(",".join(printArray), end="")
        print("]")

