def all_permutation(data):
    bUsed = [False] * len(data)
    DFS_permutation(data, [], 0, bUsed)


def DFS_permutation(data, sol, level, bUsed):
    # 종료 조건 : 임시 배열에 원소가 차면 종료
    if level == len(data):
        print(sol)
        return
    for i in range(len(data)):
        if not bUsed[i]:
            sol.append(data[i])  # 상태 업데이트 : sol에 data[i] append(), bUsed[i], level
            bUsed[i] = True
            DFS_permutation(data, sol, level+1, bUsed)  # 함수 호출
            sol.pop()  # 상태 원상복구 : sol.pop(), bUsed[i], level
            bUsed[i] = False
        
        
data = [1, 2, 3]
all_permutation(data)