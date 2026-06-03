import math
import sys
a, b, m = tuple(map(int, sys.stdin.readline().split()))

def mod(a, b, m):
    if b <= 1:
        return a % m

    elif not b % 2:
        num = mod(a, b // 2, m)
        return num * num % m

    elif b % 2:
        num = mod(a, b // 2, m)
        return ((num * num) % m) * a % m

print(mod(a, b, m))





