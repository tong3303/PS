# 한 번의 좌표 이동에 두 개 이상의 유효 좌표가 뜨면 어떻게 할까?
    # 한 개로만 쭉 가고, 다른 곳으로 가야함. => BFS가 그게 가능한가?
    # queue를 두개 쓰기? 길이 10개면 queue를 10개 써야되나? => 2차원 배열로 해결해보자.

# 좌표를 이동했을 때 유효 좌표가 하나도 뜨지 않으면, answer -= 1

# ------------------------------------------------------------------------------------------------------------
import sys
from collections import deque


def bfs():
    queue = [deque()]
    queue[0].append((0, 0))
    vis[0][0] = 1
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    answer = [0]

    for i in range(len(queue)):
        while queue[i]:
            count = 0
            cx, cy = queue[i].popleft()
            answer[i] += 1
            print(cx, ", ", cy)

            for j in range(4):
                ax = cx + dx[j]
                ay = cy + dy[j]
                if ax < 0 or ay < 0 or ax >= row or ay >= col:
                    answer[i] -= 1
                    continue

                if vis[ax][ay] == 1 or matrix[ax][ay] != "1":
                    answer[i] -= 1
                    continue

                count += 1
                vis[ax][ay] = 1

                if count > 1:
                    queue.append(deque())
                    answer.append(0)
                    queue[-1].append((ax, ay))
                else:
                    queue[i].append((ax, ay))

    return min(answer)


input = sys.stdin.readline
matrix = []

row, col = tuple(map(int, input().strip().split()))
for _ in range(row):
    matrix.append(input().strip())

vis = [[0] * col for i in range(row)]
bfs()