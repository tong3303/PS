# # 왼쪽 괄호면 stack.append(), 오른쪽 괄호면 stack.pop()
# # 이 때, (인지 [인지 확인하는 절차가 필요, ([)]도 올바른 괄호로 인식됨.
#
# # -------------------------------------------------------------------------------
# # (()[[]])([])
# # stack = ['(', '['
# # answer = 0
#
# # -------------------------------------------------------------------------------
#
# # answer  = 1
# # "(" 인지 확인한다.
#     # => stack.append()
#     # answer += 2
#
# # "["인지 확인한다.
#     # => stack.append()
#     # answer += 3
#
# # ")"이면서 stack[-1] == "("인지 확인한다.
#     # stack.pop()
#     # if stack:
#         # continue
#     # elif stack[-1] == '(":
#         # answer *= 2
#     # else:
#         # answer *= 3
#
# # "]"이면서 stack[-1] == "["인지 확인한다.
#
#
# # 아니면 0을 출력한다.
# # -------------------------------------------------------------------------------
# import sys
#
# input = sys.stdin.readline
# answer = 1
# string = "(()[[]])([])"
# stack = []
#
# for s in string:
#     if s == "(" or s == "[":
#         stack.append(s)
#     elif s == ")" and stack[-1] == "(":
#         stack.pop()
#
#         if not stack:
#             continue
#         elif stack[-1] == "(":
#             answer *= 2
#         elif stack[-1] == "[":
#             answer *= 3
#
#     elif s == "]" and stack[-1] == "[":
#         stack.pop()
#
#         if not stack:
#             continue
#         elif stack[-1] == "(":
#             answer *= 2
#         elif stack[-1] == "[":
#             answer *= 3
#
# print(answer)

# -----------------------------------------------------------------------------------------------------------
import sys

def solve():
    bracket = sys.stdin.readline().strip()
    stack = []
    answer = 0
    tmp = 1

    for i in range(len(bracket)):
        if bracket[i] == '(':
            stack.append('(')
            tmp *= 2
        elif bracket[i] == '[':
            stack.append('[')
            tmp *= 3
        elif bracket[i] == ')':
            if not stack or stack[-1] != '(':
                return 0
            if bracket[i-1] == '(':
                answer += tmp
            stack.pop()
            tmp //= 2
        elif bracket[i] == ']':
            if not stack or stack[-1] != '[':
                return 0
            if bracket[i-1] == '[':
                answer += tmp
            stack.pop()
            tmp //= 3

    return answer if not stack else 0

print(solve())