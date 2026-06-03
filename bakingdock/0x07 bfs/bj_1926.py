# 2차원 배열을 돌며 해당 좌표가 1이며, 방문하지 않았다면 BFS 알고리즘을 수행한다.
# 해당 좌표를 queue에 넣는다.
# queue.popleft()를 하며, 현재 좌표를 설정한다.

# 해당 좌표의 상, 하, 좌, 우를 확인한다.
    # 그림판의 범위를 넘지 말 것
    # 방문을 하지 않은 좌표일 것
    # 1일 것

# 위 세 과정을 통과하면, 방문했다고 표시하고 queue에 넣는다.

from collections import deque
import sys

def bfs(i, j):
    square = 1
    queue = deque()
    queue.append((i, j))
    vis[i][j] = 1
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while queue:
        cx, cy = queue.popleft()

        for _ in range(4):
            ax = cx + dxy[_][0]
            ay = cy + dxy[_][1]
            if ax < 0 or ay < 0 or ax >= row or ay >= col: continue
            if matrix[ax][ay] != 1 or vis[ax][ay] == 1: continue
            vis[ax][ay] = 1
            queue.append((ax, ay))
            square += 1
    return square


input = sys.stdin.readline
matrix = []
row, col = tuple(map(int, input().strip().split()))
count = 0
max = 0

for i in range(row):
    temp_row = list(map(int, input().strip().split()))
    matrix.append(temp_row)

vis =  [[0] * col for i in range(row)]

for i in range(row):
    for j in range(col):
        if matrix[i][j] != 1 or vis[i][j] == 1: continue
        count += 1
        square = bfs(i, j)
        if max < square:
            max = square

print(count)
print(max)

