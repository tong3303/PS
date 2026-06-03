import heapq
import sys

def dijkstra(n, adj, start):
    distances = [float('inf')] * (n + 1)
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        if curr_dist > distances[curr_node]:
            continue
        for neighbor, weight in adj[curr_node]:
            if distances[neighbor] > curr_dist + weight:
                distances[neighbor] = curr_dist + weight
                heapq.heappush(pq, (distances[neighbor], neighbor))
    return distances

def solve():
    # sys.stdin.read().split()은 대용량에서 한꺼번에 메모리를 잡아먹으므로
    # 제너레이터를 사용해 하나씩 꺼내옵니다.
    def input_generator():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = input_generator()
    
    try:
        t_str = next(tokens)
        t_cases = int(t_str)
    except StopIteration:
        return

    for _ in range(t_cases):
        n = int(next(tokens))
        m = int(next(tokens))
        k = int(next(tokens))
        
        adj = [[] for _ in range(n + 1)]
        edges = []
        for _ in range(m):
            u, v, w = int(next(tokens)), int(next(tokens)), int(next(tokens))
            adj[u].append((v, w))
            adj[v].append((u, w))
            # 규칙(1) i < j 보장
            edges.append((min(u, v), max(u, v), w))
            
        for _ in range(k):
            a, b = int(next(tokens)), int(next(tokens))
            
            dist_a = dijkstra(n, adj, a)
            dist_b = dijkstra(n, adj, b)
            
            total_l = dist_a[b]
            candidates = []
            
            # 오차 방지를 위한 아주 작은 값
            eps = 1e-7

            # 1. 모든 에지를 검사 (정점 포함)
            for u, v, w in edges:
                # 해당 에지가 최단 경로(a-b) 상에 존재하는지 확인
                # 즉, (a->u + u-v + v->b) 또는 (a->v + v-u + u->b)가 전체 최단 거리와 같은지 확인
                if abs(dist_a[u] + w + dist_b[v] - total_l) < eps or \
                   abs(dist_a[v] + w + dist_b[u] - total_l) < eps:
                    
                    # 에지 내부 혹은 정점에서 동시에 만나는 지점이 있는지 확인
                    # 각 요원이 에지의 양 끝점에 도달하는 시간 범위를 구함
                    time_a_min, time_a_max = sorted([dist_a[u], dist_a[v]])
                    time_b_min, time_b_max = sorted([dist_b[u], dist_b[v]])
                    
                    meet_time = total_l / 2
                    
                    # 만남의 시간이 두 요원 모두 해당 에지를 지나가는 시간대 안에 들어와야 함
                    if time_a_min - eps <= meet_time <= time_a_max + eps and \
                       time_b_min - eps <= meet_time <= time_b_max + eps:
                        
                        # 만약 정확히 정점에서 만난다면 (i, i) 형태로 변환
                        if abs(dist_a[u] - meet_time) < eps and abs(dist_b[u] - meet_time) < eps:
                            candidates.append((u, u))
                        elif abs(dist_a[v] - meet_time) < eps and abs(dist_b[v] - meet_time) < eps:
                            candidates.append((v, v))
                        else:
                            # 에지 중간에서 만나는 경우
                            candidates.append((u, v))

            # 2. 결과 정렬 및 중복 제거
            # 정점 만남(i, i)과 에지 만남(i, j)이 섞여 있을 수 있으므로 set으로 중복 제거 후 정렬
            final_candidates = sorted(list(set(candidates)))
            
            if final_candidates:
                res = final_candidates[0]
                sys.stdout.write(f"{res[0]} {res[1]}\n")

if __name__ == "__main__":
    solve()