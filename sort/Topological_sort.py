# 그래프 생성
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['D', 'E', 'F'],
    'D': ['G', 'H'],
    'E': ['H'],
    'F': ['G', 'H'],
    'G': [],
    'H': []
}

# in-degree가 없는 노드부터 출발
# graph[v]에 아무것도 들어있지 않는 노드를 탐색해야됨.
# graph의 정점을 모두 합친 후 중복을 제거한 뒤 graph.keys()랑 원소들을 비교해서 없는 값을 list()에 넣음.
zero_indegree = []
tmp = []
for v in graph.values():
    tmp += v

for k in graph.keys():
    if not k in tmp:
        zero_indegree.append(k)

# DFS에서 a : ['b', 'c'] 이런 형태로 되어 있을 때 모두 방문하면, list.append('a')
topological_sort = []
visited = {k:False for k in graph.keys()}

def DFS(node):
    visited[node] = True
    for out_de in graph.get(node, []):
        if visited.get(out_de, False): continue
        DFS(out_de)
    topological_sort.append(node)

# 이 과정을 list에 모든 노드들이 들어올 때까지 진행하면 됨.
for z in zero_indegree:
    if visited[z]:  continue
    DFS(z)

topological_sort.reverse()
print(topological_sort)
