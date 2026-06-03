import sys
from collections import deque

input = sys.stdin.readline
col, row = tuple(map(int, input().strip().split()))

matrix = []
vis = []
for r in range(row):
    tempMatrix = list(map(int, input().strip().split()))
    matrix.append(tempMatrix)

    tempVis = [-1 if matrix[r][c] == -1 else 0 for c in range(col)]
    vis.append(tempVis)

queue = deque()

for r in range(row):
    for c in range(col):
        if matrix[r][c] == 1:
            vis[r][c] = 1
            queue.append((r, c))

while queue:
    cx, cy = queue.popleft()
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)

    for i in range(4):
        ax = cx + dx[i]
        ay = cy + dy[i]
        if ax < 0 or ay < 0 or ax >= row or ay >= col: continue
        if matrix[ax][ay] == -1: continue
        if vis[ax][ay] == 0:
            queue.append((ax, ay))
            vis[ax][ay] = vis[cx][cy] + 1

for r in range(row):
    if 0 in matrix[r]:
        print(-1)
        break
else:
    print(vis[ax][ay] - 1)


