row, col = 5, 5

graph = [[0] * (col+1) for i in range(row+1)]
vis = [False for i in range(row+1)]
print(vis)

def DFS(node):
    vis[node] = True
    print(node)

    for i in range(1, row+1):
        print(node, "  ", i)
        if graph[node][i] == 1:  # node와 연결된 모든 간선 확인
            if vis[i]: continue
            DFS(i)

graph[1][1] = 1
graph[1][2] = 1
graph[1][3] = 1
graph[2][3] = 1

DFS(1)