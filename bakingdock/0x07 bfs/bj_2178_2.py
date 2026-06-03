import sys
from collections import deque

def bfs():
    queue = deque()
    queue.append((0, 0))
    vis[0][0] = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            ax = cx + dx[i]
            ay = cy + dy[i]

            if ax < 0 or ay < 0 or ax >= row or ay >= col: continue
            if matrix[ax][ay] != "1" : continue
            num = vis[cx][cy]
            if vis[ax][ay] == -1:
                vis[ax][ay] = vis[cx][cy] + 1
                queue.append((ax, ay))

    return vis[row-1][col-1]

input = sys.stdin.readline
matrix = []

row, col = tuple(map(int, input().strip().split()))
for _ in range(row):
    matrix.append(input().strip())

vis = [[-1] * col for i in range(row)]
print(bfs() + 1)