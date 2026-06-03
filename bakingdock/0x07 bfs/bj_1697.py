import sys
from collections import deque

N, K = tuple(map(int, sys.stdin.readline().split()))
vis = [-1 for i in range(1000001)]
vis[N] = 0
queue = deque()
queue.append(N)
dx = [-1, 1]

while queue:
    cx = queue.popleft()
    dx.append(cx)

    for i in range(3):
        ax = cx + dx[i]
        if ax < 0 or ax > 100000: continue
        if vis[ax] == -1:
            vis[ax] = vis[cx] + 1
            queue.append(ax)

    dx.pop()

    if vis[K] != -1:
        print(vis[K])
        break