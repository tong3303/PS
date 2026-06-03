matrix = [
    [0, 1, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 1, 1, 1, 1]
]

vis = set()
stack = []
dy = [1, 0, -1, 0]   # 행 이동 (아래, 없음, 위, 없음)
dx = [0, 1, 0, -1]   # 열 이동 (없음, 오른쪽, 없음, 왼쪽)


def find_start():
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                return i, j
    return None


def dfs(i, j):
    row = len(matrix)
    col = len(matrix[0])

    stack.append((i, j))
    vis.add((i, j))

    while stack:
        y, x = stack.pop()
        print(y, ",", x)

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if ny < 0 or ny >= row or nx < 0 or nx >= col: continue
            if (ny, nx) in vis or matrix[ny][nx] == 0: continue

            vis.add((ny, nx))
            stack.append((ny, nx))


if __name__ == "__main__":
    result = find_start()
    if result:
        i, j = result
        dfs(i, j)