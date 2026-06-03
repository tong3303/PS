# 좋은 글자의 규칙 찾기
# ABBA => (O) 각 알파벳의 짝수 번째 알파벳은 stack[top]과 항상 동일해야한다.
# AAA => (X) 문자열이 모두 입력된 후 stack.empty()는 true

# -----------------------------------------------------------------
# 각 알파벳의 등장 횟수를 세는 변수를 만든다.
# 각 알파벳의 등장했던 횟수가 짝수면, 스택에 값을 넣고, 등장 횟수를 추가한다.
# 각 알파벳의 등장했던 횟수가 홀수면, 가장 최근에 넣은 값과 현재 값을 비교한다.
    # 같다. => 스택에서 없애고, 등장 횟수를 추가한다.
    # 다르다 => 제대로 되지 않은 문자니 반복문을 종료하고, 좋지 않은 문자라고 체크한다.

# 반복문이 끝나면 스택이 비었는지 확인한다.
    # ture => pass
    # false => 안좋은 단어라고 체크

# 좋은 단어인지 안좋은 단어인지 판단 후 count += 1
# ==> 반례 ABAABA 지금 등장한 알파벳이 stack에 넣어야하는지, 삽입해야하는지 판단하는 기준이 "등장 횟수는" 아님.
# -----------------------------------------------------------------

import sys
input = sys.stdin.readline
answer = 0
word_amount = int(input())
for i in range(word_amount):

    word = input().strip()  # ABAABA
    A_num = 0  # 1
    B_num = 0  # 1
    stack = []  # [A]
    is_good = True

    for alphabet in word:  # A
        if alphabet == "A" and A_num % 2 == 0:
            stack.append(alphabet)
            A_num += 1

        elif alphabet == "A" and A_num % 2 != 0:
            if stack[-1] != alphabet:
                is_good = False
                break

            stack.pop()
            A_num += 1

        elif B_num % 2 == 0:
            stack.append(alphabet)
            B_num += 1

        else:
            if stack[-1] != alphabet:
                is_good = False
                break

            stack.pop()
            B_num += 1

    if len(stack):
        is_good = False

    if is_good:
        answer += 1

print(answer)