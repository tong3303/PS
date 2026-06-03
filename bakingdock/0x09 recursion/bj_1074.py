import sys

n, target_row, target_col = tuple(map(int, sys.stdin.readline().strip().split()))
count = 0

def recursion_Z(n, start):
    if n == 1:
        dx = (0, 1, 0, 1)
        dy = (0, 0, 1, 1)

        for i in range(4):
            ax = start[0] + dx[i]
            ay = start[1] + dy[i]

            if (ay, ax) == (target_row, target_col):
                return i
    
    else:
        step = 2^(n-1)
        dx = (0, step, 0, step)
        dy = (0, 0, step, step)

        for i in range(4):
            ax = start[0] + dx[i]
            ay = start[1] + dy[i]
            recursion_Z(n-1, (ay, ax))

            

# 1. 내가 짠 함수의 종료 조건은 어떻게 되지?
# - n이 1일 때 dx, dy로 좌표를 확인한 후 종료한다. => O(1), T(0) = 4

# 2. T(n)과 T(n-1)의 관계는 어떻지?  T(n) = 4T(n-1)

# 3. dx, dy를 어떻게 설정할까?
# T(1) => 1, T(2) => 2, T(3) => 4, T(4) => 8
# T(n) => 2^n-1

# 4. count를 어떻게 할까?
# 

# ----------------------------------------------------------------------------------------------------------------------------------------------------
# 모든 사분면을 방문하지 않고, 답을 도출해내는 방법이 있었음. => gemini
count = 0

def recursion_Z_answer(n, y, x):
    if n == 0:
        return

    global count
    r = 2**(n-1)
    s = r * r

    if target_row < y + r and target_col < x + r:
        recursion_Z_answer(n-1, y, x)
    
    elif target_row < y + r and target_col >= x + r:
        count += s
        recursion_Z_answer(n-1, y, x+r)
    
    elif target_row >= y + r and target_col < x + r:
        count += 2*s
        recursion_Z_answer(n-1, y+r, x)
    
    else:
        count += 3*s
        recursion_Z_answer(n-1, y+r, x+r)

recursion_Z_answer(n, 0, 0)
print(count)
    