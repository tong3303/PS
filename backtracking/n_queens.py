# def all_n_queen(n):
#     maze = [[0] * n for _ in range(n)]
#     DFS_n_queen(n, maze, 0, 0)


# def DFS_n_queen(n, maze, x, y):
#     check_safe = [False, False, False]
#     if not is_safe(n, maze, x, y, 1, check_safe):
#         return

#     if y == n-1:  마지막 행에 도달했을 때 바로 출력 => 퀸을 마지막 행에 놓지 않았음.
#         print(maze)
#         return

#     maze[y][x] = 1  반복문 내에 이 과정을 안넣으니 0열만 조사하게 됨.
#     for i in range(n):
#         DFS_n_queen(n, maze, 0, y+1)
#     maze[y][x] = 0


# def is_safe(n, maze, x, y, i, check_safe):  for문을 잘 활용하자. 
#     cx = [-1, 0, 1]
#     cy = [-1, -1, -1]

#     cx = list(map(lambda x:x*i, cx))
#     cy = list(map(lambda x:x*i, cy))

#     for j, (ax, ay) in enumerate(zip(cx, cy)):
#         if x+ax < 0 or x+ax >= n or y+ay < 0:
#             check_safe[j] = True
#             continue

#         elif maze[y+ax][x+ax] == 1:  y+ay라고 적어야하는데, 오타를 발견하지 못함.
#             return False
    
#     if False not in check_safe:
#         return True
#     return is_safe(n, maze, x, y, i+1, check_safe)


# n = 4
# all_n_queen(4)


def is_safe(board, x, y):
    N = len(board)

    for i in range(y):
        if board[i][x] == 1: return False  # 세로 방향 검사
    for i, j in zip(range(y-1, -1, -1), range(x-1, -1, -1)):
        if board[i][j] == 1: return False  # 왼쪽 대각선 검사
    for i, j in zip(range(y-1, -1, -1), range(x+1, N)):
        if board[i][j] == 1: return False
    return True


def solve_N_queen(board, y):
    N = len(board)
    if y == N:
        print_board(board)
        return
    
    for x in range(N):
        if is_safe(board, x, y):
            board[y][x] = 1
            solve_N_queen(board, y+1)
            board[y][x] = 0


def print_board(board):
    N = len(board)
    print_board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                print_board[i][j] = '.'
            else:
                print_board[i][j] = 'Q'
    
    print("board 출력")
    for i in print_board: print(i)

N = 4
board =[[0] * N for _ in range(N)]
solve_N_queen(board, 0)