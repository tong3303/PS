# (matrix, vis) : (0, 0), (0, 1), (1, 0), (1, 1)

import sys
from collections import deque
import time

start = time.time()

input = sys.stdin.readline
rowCol = int(input())
matrix = []

for i in range(rowCol):
    tempRow = list(map(int, list(input().strip())))
    matrix.append(tempRow)

danji = []
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

# vis = [[0] * rowCol for i in range(rowCol)]
vis2 = set()

for i in range(rowCol):
    for j in range(rowCol):

        if matrix[i][j] == 0 or (i, j) in vis2:  # (1, 0)만 통과 가능
            continue

        count = 1
        queue = deque()
        queue.append((i, j))  # ((1, 1))
        vis2.add((i, j))

        while queue:
            cx, cy = queue.popleft()
            # count += 1

            for _ in range(4):
                ax = cx + dx[_]
                ay = cy + dy[_]
                if ax < 0 or ay < 0 or ax >= rowCol or ay >= rowCol: continue
                if matrix[ax][ay] == 0 or (ax, ay) in vis2: continue
                queue.append((ax, ay))
                vis2.add((ax, ay))
                count += 1
                # vis[ax][ay] = 1

            # queue가 비어 있다. => 범위 벗어남 + 이미 방문함 + 1이 없음. => 인접한 모든 좌표를 방문함.
            # danji에 추가하면 됨. => 문제가 없는 거 같음.

        danji.append(count)

danji.sort()
print(len(danji))
for i in danji:
    print(i)
end = time.time()
