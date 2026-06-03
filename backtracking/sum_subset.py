def all_subset(data, M):
    sub = []
    remaining = sum(data)
    DFS_subset(data, M, 0, sub, remaining)

''' 집합은 순서가 없으므로 bUsed로 중복을 막는건 안됨.
def DFS_subset(data, M, sub, bUsed, sum):
    if M == sum:
        print(sub)
        return
    for i in range(len(data)):
        if sum < M and not bUsed[i]:
            sub.append(data[i])
            bUsed[i] = True
            DFS_subset(data, M, sub, bUsed, sum+data[i])
            sub.pop()
            bUsed[i] = False
'''

# remaining : 지금 level 뒤부터 끝까지의 합
def DFS_subset(data, M, level, sub, remaining):
    if sum(sub) == M:
        print(sub)
        return
    
    if sum(sub) > M or (remaining + sum(sub)) < M:
        return
    
    for i in range(level, len(data)):
        sub.append(data[i])
        DFS_subset(data, M, i+1, sub, remaining-data[i])
        sub.pop()

data = [1, 4, 3, 5, 2, 6, 8]
M = 5
all_subset(data, M)