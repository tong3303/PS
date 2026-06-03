# 그래프를 인접 리스트로 표현하는 방법
row, col = 5, 5
graph = {i: [] for i in range(1, row+1)}
print(graph)

# claude가 추천한 방식
# 이 때, 0번 인덱스는 사용하지 않음. => idx - 1은 위험
graph_list = [[] for i in range(row)]



    
    