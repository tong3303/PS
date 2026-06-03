# 문제 있음
from collections import deque

n = 10
graph = [[] for i in range(n)]
visited = []
queue = deque()


def bfs(start):
    queue.append(start)
    
    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        visited.append(v)
        nghs = graph[v] - visited
        for ngh in nghs:
            queue.append(ngh)
