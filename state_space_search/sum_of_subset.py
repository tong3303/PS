# def solve(s, goal, tmp_li, li, level):
#     # 현재 상태가 종료 상태인지 확인한다.  (현재까지의 부분합 == 목표값)
#     # 1. s : 현재까지의 부분합
#     # 1. goal : 목표값
#     # 2. 뭐를 반환하는거지? 숫자들의 조합을 반환해야됨. => 현재까지의 숫자 리스트를 저장해야됨.
#     if s == goal:
#         return tmp_li
    
#     if level == len(li):
#         return  # 6. s == goal에서 return이 안되었으니 정답이 아님.

#     # 현재 상태에서 전이 행동들을 모두 수행한다.
#     # 3. tmp_li에 어떤 숫자를 넣어야하지? => 원본 리스트 필요 => li
#     # 4. li에서 현재 넣어야 하는 숫자가 뭐지? => level
#     key = li[level]  # 5. 모든 물건을 다 넣으면 종료가 되어야 됨.
#     solve(s, goal, tmp_li, li, level+1)
#     tmp_li.append(key)
#     solve(s+key, goal, tmp_li, li, level+1)

# li = [1, 4, 3, 2, 5]
# res = solve(0, 5, [], li, 0)
# print(res)

# 7. None이 리턴이 됨. => 트리의 첫번째 leaf node가 정답이 아니면 제대로 된 답이 안나오도록 설계가 되어 있음.
# => 전이 과정이 부족했다고 판단을 내림. 전이를 한 후 돌아오는 과정은 설계가 되어있지 않음.

# 힌트를 본 후 변한 생각 => 답을 출력하는게 아니라 경우의 수를 세는 문제였음.
# tmp_li는 필요없고, 최종적으로 정답이 몇개인지 세는 변수가 필요.


# def solve(curr_s, goal, global_set, level, count):
#     ''' curr_s : 현재 부분합, goal : 목표 합, global_set : 숫자 후보들, 
#     level : 순회 단계, count : curr_s == goal 일치 갯수'''
#     # if curr_s == goal:  # 어떤 반환값을 뱉어야 하지? count가 더해져야함. 하지만 return count + 1을 하면 안됨. solve(..., count+1)을 한 후 종료 조건을 하나 더 만들어야 할 듯
#     #     # return solve(curr_s, goal, global_set, level, count + 1)  # level + 1도 필요한가?  [3, 4, 2, 1, 5]이고, 그대로 진행 => (4, 1)을 놓침. 0으로 초기화 => (3, 2)로 무한루프
#     #     count += 1
    
#     # if level == len(global_set):
#     #     return count

#     # 2. leaf node에 도착했을 때 리턴을 해야 중복 count가 없어진다고 판단 => 결과가 1로 나옴.
#     if curr_s == goal and level == len(global_set):
#         return count + 1
#     elif level == len(global_set):
#         return count
    
#     res1 = solve(curr_s + global_set[level], goal, global_set, level+1, count)
#     res2 = solve(curr_s, goal, global_set, level+1, count)

#     return max(res1, res2)

# global_set = [1, 4, 3, 2, 5]
# res = solve(0, 5, global_set, 0, 0)
# print(res)  # 1. 3이 아닌 4가 리턴이 됨. 왜 막혔지? 종료 시점에서 중복 카운트가 문제라고 판단.  42~45줄로 고침.  => 카운트를 함수 내에서 고치니 수정한 값이 반영되지 않음. => 기저 조건을 잘못 세움.

# 정답
def solve(s, goal, li, level):
    if s == goal:
        sum[0] += 1
        return
    
    if level == len(li):
        return

    solve(s+li[level], goal, li, level+1)
    solve(s, goal, li, level+1)

sum = [0]
li = [3, 2, 4, 1, 5]
goal = 5
solve(0, goal, li, 0)
print(sum[0])