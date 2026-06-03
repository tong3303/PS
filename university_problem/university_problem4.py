import sys

def create_shift_table():
    pass

def main():
    input = sys. stdin. readline
    case = int(input())

    for _ in range(case):
        s1 = [int(input()) for i in range(case)]
        s2 = [int(input()) for i in range(case)]
        R = [-i for i in s2[ ::- 1]] # s2 역방향 조사
        s1 += s1