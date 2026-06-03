# def all_find_maze(maze):
#     answer = []
#     dy_dx = [(1, 0, -1, 0), (0, 1, 0, -1)]
#     visited = [[False] * len(maze[0]) for _ in range(len(maze))]
#     DFS_find_maze(maze, len(maze), len(maze[0]), dy_dx, 0, 3, answer, visited)


# def is_in_boundary(h, w, ay, ax):
#     return ay >= 0 and ay < h and ax >= 0 and ax < w


# def DFS_find_maze(maze, h, w, dy_dx, y, x, answer, visited):
#     if maze[y][x] == 2:
#         print(answer)
#         return
    
#     for i in range(4):
#         ay = y + dy_dx[0][i]
#         ax = x + dy_dx[1][i]
#         # print(ay, ax)
#         if is_in_boundary(h, w, ay, ax) and maze[ay][ax] == 1 and not visited[ay][ax]:
#             answer.append((ay, ax))
#             visited[ay][ax] = True
#             DFS_find_maze(maze, len(maze), len(maze[0]), dy_dx, ay, ax, answer, visited)
#             answer.pop()
#             visited[ay][ax] = False  이거만 없었으면 풀었을듯?


# maze = [[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
#         [0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0],
#         [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
#         [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
#         [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 2],
#         [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
#         [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
#         [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]

# all_find_maze(maze)


def solve_maze(maze, x, y):
    W, H = len(maze[0]), len(maze)
    sol = [[0] * W for i in range(H)]  # 경로 저장
    mark = [[0] * W for i in range(H)]  # 방문 여부

    if DFS_maze(maze, x, y, sol, mark) == False:
        print("출구를 찾을 수 없음")
    else:
        for i in sol: print(i)


def is_safe(maze, x, y, mark):
    W, H = len(maze[0]), len(maze)
    if x >= 0 and x < W and y >= 0 and y < H:
        if maze[y][x] != 0 and mark[y][x] == 0:
            return True
    return False


def DFS_maze(maze, x, y, sol, mark):
    W, H = len(maze[0]), len(maze)

    # 조건 검사
    if not is_safe(maze, x, y, mark):
        return
    
    # 상태 업데이트
    mark[y][x] = 1
    sol[y][x] = 1
    if maze[y][x] == 2:
        return True
    
    # 상태 업데이트 + 함수 호출
    if DFS_maze(maze, x+1, y, sol, mark): return True
    if DFS_maze(maze, x, y+1, sol, mark): return True
    if DFS_maze(maze, x-1, y, sol, mark): return True
    if DFS_maze(maze, x, y-1, sol, mark): return True

    # 상태 원복
    sol[y][x] = 0
    # mark[y][x] = 0  이 문제를 처음 풀 때, 방문 여부를 취소해야된다고 생각했음. => 취소를 안하면 이 길이 아닐 때 어쩌지? 
    # => 이미 방문 후 재귀로 들어갔기 때문에 재귀가 되돌아가는 것으로 길을 되돌아가는 효과가 있음.
    return False

maze = [[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 2],
        [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]

solve_maze(maze, 3, 0)