from collections import deque

# 1이 방문해야 되는 곳, 0이 방문하지 않아도 되는 곳
board = [
    [1,1,1,0,1,0,0,0,0,0],
    [1,0,0,0,1,0,0,0,0,0],
    [1,1,1,0,1,0,0,0,0,0],
    [1,1,0,0,1,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

row, col = 7, 10  # 행의 수
vis = [[0] * col for i in range(row)]

# 상하좌우 네 방향을 의미
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

queue = deque()
vis[0][0] = 1  # 0, 0에서 시작했다고 가정
queue.append((0, 0))

while queue:
    cx, cy = queue.popleft()

    print('(', str(cx), ", ", str(cy), ") -> ")
    for i in range(4):
        nx = cx + dxy[i][0]
        ny = cy + dxy[i][1]
        if nx < 0 or ny < 0 or nx >= row or ny >= col: continue
        if vis[nx][ny] == 1 or board[nx][ny] != 1: continue
        vis[nx][ny] = 1
        queue.append((nx, ny))



