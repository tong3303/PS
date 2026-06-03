# n부터 1까지의 합을 구하는 재귀함수
def n_to_one(n):
    if n == 0:
        return n
    else:
        return n + n_to_one(n-1)

# 1부터 n까지의 합을 구하는 재귀함수
def one_to_n(n, m):
    if n == m:
        return n
    else:
        return one_to_n(n + 1, m) + n
    
print(one_to_n(1, 5))

