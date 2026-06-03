# num[0] => n [1, 2, ..., n-1]
# num[1] => 반복문
# 반복문에서 밑에 주어진 숫자를 빼는 최소한의 로직을 작성한다.
# 1. 바로 뺄 수 있나? => 바로 뽑고 continue 진행한다. head와 뽑아야 할 숫자가 일치하는지 확인
# 2. 왼쪽으로 돌리는게 이득인가? num[0]을 토대로 판단하면 안됨 => 회전했을 수도 있기 때문에
# head가 뭔지 기억하고 있어야함! => abs(head - 뽑아야 할 숫자) < num[0] => 이득
# 위 조건을 만족하지 않으면 오른쪽으로 돌리는게 이득임.
# -------------------------------------------------------------------------------------------------------------

# total_array_len = num[0] 배열의 길이
# total_pop_num = num[1] 뽑아야 할 횟수
# pop_array = 뽑아야 할 숫자들의 모음
# pop_num = pop_array를 반복하며 나오는 요소
# head = total_array의 head
# rotate_count = 회전할 숫자 체크
# --------------------------------------------------------------------------------------------------------------

# 1. for문이 아니라 while문으로 작성해야 됨
# 2. head만 사용하면 rotate가 아니라 pop만 되기에 rear도 통제해줘야 됨.
# 3. head가 rear가 1~total_array_len의 범위를 넘어가지 않도록 값 변경을 해줘야 됨
# 4. head를 +, - 해주는 거론 삭제된 요소들을 반영할 수 없음. deque 모듈을 사용해야됨 => head, rear는 따로 필요 없음.
# 5. abs(head - 뽑아야 할 숫자) < num[0] 이 제대로 된 조건이 아님. abs(head - pop_num) < len(deq) // 2가 되는게 맞긴한데, 무한루프에 걸릴 수도 있을듯.
# 6. 답을 확인하니 그냥 인덱스 위치를 찾아서 왼쪽, 오른쪽의 효율을 판단했음. => index 탐색이 O(n)이니 사용하지 않으려고 했는데, 이 생각이 문제 해결을 어렵게 만든 거 같음.
# => 여러가지 에로 사항이 있었지만, 핵심 문제는 어느 방향으로 rotate를 진행하는게 효율적인지 판단하는 로직을 구현하는 것이었음. 핵심 문제가 뭔지 빠르게 판단하면 머리를 덜 쓰면서
# 문제 해결이 가능할듯.
# --------------------------------------------------------------------------------------------------------------
import sys
from collections import deque

temp_num = tuple(map(int, sys.stdin.readline().strip().split()))  # 10 3
total_array_len = temp_num[0]; total_pop_num = temp_num[1]  # 10, 3
pop_array = tuple(map(int, sys.stdin.readline().strip().split()))  # 2, 9, 5
rotate_count = 0
idx = 0
deq = deque([i for i in range(1, total_array_len + 1)])

while idx < total_pop_num:  # 2 < 3
# for pop_num in pop_array:
    pop_num = pop_array[idx]  # 5

    if pop_num == deq[0]:  # 5 == 10
        deq.popleft()  # [10, 1, 3, 4, ....]
        idx += 1  # 2

    elif deq.index(pop_num) < len(deq) // 2:
    # elif abs(deq[0] - pop_num) < len(deq) // 2:  # abs(5 - 10) < 8  => 이 조건 제대로 된 거 맞나?
        deq.rotate(-1)  # [10, 1, 3, 4, ....]
        rotate_count += 1  # 4

    else:
        deq.rotate(1)
        rotate_count += 1

print(rotate_count)
