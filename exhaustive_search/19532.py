import sys

ex_input = list(map(int, sys.stdin.readline().strip().split()))
ex1 = ex_input[:3]
ex2 = ex_input[3:]

mul_num = ex1[0] / ex2[0]
ex2 = list(map(lambda x: -mul_num * x, ex2))
ex3 = [ex1[i] + ex2[i] for i in range(3)]  # [0, n, m]
div_num = ex3[1] / 1
answer = ['x', ex3[2]/div_num]
ex1[1] = ex1[1] * answer[1]
ex1[2] = ex1[2] - ex1[1]
div_num = ex1[0] / 1
ex1[2] = ex1[2] / div_num
answer[0] = ex1[2]
answer = list(map(lambda x: int(x), answer))
print(*answer)