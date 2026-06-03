# stack[-1]과 넣고자 하는 알파벳이 같으면 stack.pop()
# stack[-1]과 넣고자 하는 알파벳이 다르면 stack.append()

# 모든 알파벳을 넣은 후 len(stack) == 0이면 answer += 1
import sys

input = sys.stdin.readline
answer = 0
word_amount = int(input())

for i in range(word_amount):
    word = input().strip()
    stack = []

    for w in word:
        if not stack:
            stack.append(w)

        elif stack[-1] == w:
            stack.pop()

        else:
            stack.append(w)

    if not stack:
        answer += 1

print(answer)