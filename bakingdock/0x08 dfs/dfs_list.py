import sys
sys.setrecursionlimit(10000)
n = 10

graph = [[] for i in range(n+1)]
vis = set()

# recursion
def dfs(node):
    # 1. 베이스 조건 : 가장 단순한 인풋은 무엇인가?
    # => graph에 모든 값이 비어있는 경우 => node와 인접한 노드가 없는 것
    # => node의 리스트가 비어있을 때를 뜻함.

    # 2. 분해 : 베이스 조건에 가까워지도록 인풋값을 조작한다.
    # => graph[node]에 하나의 원소만 있는 경우
    # graph[node]를 출력하고, graph[graph[node]]가 비어있다면? 종료

    # graph[node]에 두개의 원소만 있는 경우
    # graph[node]를 출력하고, graph[graph[node]]가 비어있다.
    # graph[node+1]를 출력하고, graph[graph[node+1]]가 비어있다.

    print(node)
    vis.add(node)

    for next_node in graph[node]:
        if next_node in vis:
            dfs(next_node)

graph[1].append(2)
graph[2].append(3)
graph[2].append(4)
graph[3].append(5)
dfs(1)
