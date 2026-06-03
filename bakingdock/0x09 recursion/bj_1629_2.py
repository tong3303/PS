import sys


def BJ_1629(a, b, m):
    # (a * b) % m == ((a % m) * (b % m)) % m
    if b <= 1:
        return a % m

    elif not b % 2:
        result = BJ_1629(a, b//2, m)
        return (result * result) % m

    else:
        result = BJ_1629(a, b // 2, m)
        return (result * result * a) % m


if __name__ == "__main__":
    a, b, m = tuple(map(int, sys.stdin.readline().strip().split()))
    answer = BJ_1629(a, b, m)
    print(answer)

