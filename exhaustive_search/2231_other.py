# 다른 사람의 풀이를 참조했음.

import sys

n = int(sys.stdin.readline())
div_sum = 0

for i in range(n-54, n):
    k = i
    sum = 0

    while k > 0:
        sum += k % 10
        k //= 10

    if i+sum == n:
        div_sum = i
        break

print(div_sum)