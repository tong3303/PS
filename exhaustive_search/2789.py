import sys

input = sys.stdin.readline
n, m = tuple(map(int, input().strip().split()))
card = list(map(int, input().strip().split()))


max_sum = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            current_sum = card[i] + card[j] + card[k]
            if current_sum <= m:
                max_sum = max(max_sum, current_sum)

print(max_sum)