# def DFS_find_color_graph(graph, color, node):
#     N = len(graph)
    
#     if node == N:
#         print(color)
#         return 밑 코드처럼 최소 정답만 출력되도록 설계했다면
#                순열처럼 번호만 바뀐채 정답이 나오지 않았을 것

#     for i in range(N):
#         color[node] = i
#         is_overlap = find_ngh_color(graph, color, node)
#         if not is_overlap:
#             DFS_find_color_graph(graph, color, node + 1)
#             color[node] = -1


# def find_ngh_color(graph, color, node):
#     N = len(graph)
#     for i in range(N):
#         if i == node: continue
#         if (color[i] == color[node]) and (color[i] != -1):
#             return True
#     return False


def all_find_color_graph(graph):
    N = len(graph)
    color = [0] * N
    if DFS_graph_coloring(graph, 4, 0, color):
        print("그래프 색칠 성공:", color)
    else:
        print("색칠 가능한 방법이 없습니다.")


def is_safe(graph, v, c, color):
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True


def DFS_graph_coloring(graph, k, v, color):
    if v == len(graph):
        return True
    for c in range(1, k+1):
        if is_safe(graph, v, c, color):
            color[v] = c
            if DFS_graph_coloring(graph, k, v+1, color):
                return True
            color[v] = 0
    return False


graph = [
    [0, 1, 1, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [0, 0, 1, 0]
]
all_find_color_graph(graph)