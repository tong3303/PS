import sys
from collections import deque

# input
input = sys.stdin.readline
vertex, edge, start = tuple(map(int, input().strip().split()))

# graph, vis
graph = [[] for i in range(vertex + 1)]
vis = [False for i in range(vertex + 1)]

# edge
for _ in range(edge):
    i, j = tuple(map(int, input().strip().split()))
    if i != j:  # cycle 대비   
        graph[i].append(j)
        graph[j].append(i)
    else:
        graph[i].append(j)

for _ in range(vertex):
    graph[_].sort()

# dfs
def dfs(vertex):
    vis[vertex] = True
    print(vertex, end=" ")

    for next in graph[vertex]:
        if not vis[next]:
            dfs(next)

# bfs
def bfs(start):
    vis = [False for i in range(vertex + 1)]
    
    if start in graph[start]: graph[start].remove(start)  # 자기 자신이 들어가는 경우
    # graph[start] = list(set(graph[start]))  # 같은 값이 들어가는 경우
    # graph[start].sort()
    queue = deque(graph[start])
    vis[start] = True
    print(start, end=" ")

    while queue:  # queue가 비었는데, 방문하지 못하는 경우가 있을까?
        current_vertex = queue.popleft()
        if vis[current_vertex]: continue
        vis[current_vertex] = True
        print(current_vertex, end=" ")

        for i in graph[current_vertex]:
            if not vis[i] and i not in queue:  # 이 부분은 맞다고 생각함. => 방문하지 않았다. [queue에 있다, 인접한 노드가 queue에서 pop되지 않았다.]
                queue.append(i)

dfs(start); print()
bfs(start)