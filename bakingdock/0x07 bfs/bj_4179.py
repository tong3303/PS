import sys
from collections import deque

def bfs(target, vis):
    FJ = []
    if target == "F":
        for i in range(row):
            if matrix[i].find("F") != -1:  # 같은 줄에 여러 개의 불이 있을 수 있음.
                j = matrix[i].find("F")
                FJ.append((i, j))

    else:
        for i in range(row):
            if matrix[i].find("J") != -1:
                j = matrix[i].find("J")
                FJ.append((i, j))
                break

    for _ in range(len(FJ)):
        i = FJ[_][0]
        j = FJ[_][1]

        queue.append((i, j))

        vis[i][j] = 0

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            ax = cx + dx[i]
            ay = cy + dy[i]
            if ax < 0 or ay < 0 or ax >= row or ay >= col: continue
            if matrix[ax][ay] == "#": continue
            if vis[ax][ay] == -1:
                vis[ax][ay] = vis[cx][cy] + 1
                queue.append((ax, ay))


def move():
    for i in range(row):
        if 0 in visJ[i]:
            j = visJ[i].index(0)

    queue = deque()
    queue.append((i, j))
    visMove[i][j] = 1

    while queue:
        cx, cy = queue.popleft()

        for _ in range(4):
            ax = cx + dx[_]
            ay = cy + dy[_]

            if ax < 0 or ay < 0 or ax >= row or ay >= col:
                print(visJ[cx][cy] + 1)
                return 0

            if visJ[ax][ay] == -1: continue
            if visMove[ax][ay] == 1: continue
            if visJ[ax][ay] < visF[ax][ay]: continue  # 2 < 1: true로 인식됨 ==> 이미 불이 있는데 뛰어듦. vis를 매우 큰 숫자로 초기화

            queue.append((ax, ay))
            visMove[ax][ay] = 1

    print("IMPOSSIBLE")
    return 0


input = sys.stdin.readline
row, col = tuple(map(int, input().strip().split()))
matrix = []

for r in range(row):
    tempRow = input().strip()
    matrix.append(tempRow)

visJ = [[-1] * col for i in range(row)]
visF = [[-1] * col for i in range(row)]
visMove = [[0] * col for i in range(row)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

queue = deque()

bfs("F", visF); print(visF)
bfs("J", visJ); print(visJ)
move()

