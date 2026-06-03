# 1 ~ N까지 반복을 진행해야 됨. => i
# L : 비교해야되는 숫자의 갯수
# [i-L] ~ [i-1]까지를 비교하는데, idx >= 0인 애들만 비교 대상
# 이게 왜 덱 문제일까?
# -----------------------------------------------------

# deque의 길이를 확인하고, deque의 길이가 L과 같으면, 가장 먼저 들어온 원소를 pop => O(1)
# 원소 한개를 deque 넣는다. => O(1)
# deque에서 최솟값을 출력한다. => O(L)

# deque의 길이를 확인하고, deque의 길이가 L과 같으면, 가장 먼저 들어온 원소를 pop
# 원소 한개를 deque 넣는다.
# deque에서 최솟값을 출력한다.

# deque의 길이를 확인하고, deque의 길이가 L과 같으면, 가장 먼저 들어온 원소를 pop
# 원소 한개를 deque 넣는다.
# deque에서 최솟값을 출력한다.

# ==> O(L) * N 최선인가? 이렇게 문제를 해결하면 deque가 아닌 list로 해도 됨.  ==> 시간 부족이 뜰듯

# 정렬하기? : 정렬을 하고, 최솟값을 출력, 빼야 하는 원소는 기존의 배열에서 확인
# 정렬 O(L log L) + 최솟값 출력 O(1) + 빼야 하는 원소 확인 후 제거 O(L) => 손해

# 최솟값 기억하기 : 비교를 끝낸 후 최솟값을 기억해 들어오는 원소와 바로 비교
# 최솟값이 빠져나갔는지 기억하는 시간복잡도 O(1) => deque[0] == min && len(deque) == 3이면 최솟값을 다시 찾으면 됨.
# --------------------------------------------------------

# N, L을 입력받고, 특수 문자 제거 등 전처리
# N 배열을 받고 마찬가지로 전처리 => arr

# min = deq[0]
# N번 반복을 수행함.
    # 길이가 아직 3이 아닐때 처리하는 로직 [deq의 길이가 3보다 작다면]
    # deq.append(arr[i])
    # if min > arr[i]: min = arr[i]
    # print(min)

    # 최솟값이 변경될 때 [min == deq[0] elif로 묶을거기 때문에 길이를 비교하는 연산은 필요없을듯?
    # deq.popleft()
    # deq.append(arr[i])
    # deq.최솟값 탐색 및 min에 재할당
    # print(min)


    # 최솟값이 변경되지 않을 때  [else] => deq의 길이가 3보다 크거나 같고, 최솟값이 pop되지 않을때
    # deq.popleft()
    # deq.append(arr[1])
    # if min > arr[i]: min = arr[1]
    # print(min)

# -------------------------------------------------------------------------------------------------------------
# import sys
# from collections import deque
#
# N_L = list(map(int , sys.stdin.readline().strip().split()))
# arr = list(map(int , sys.stdin.readline().strip().split()))
# deq = deque()
# min_num = arr[0]
#
# for num in arr:
#
#     if len(deq) < N_L[1]:
#         deq.append(num)
#         if min_num > num: min_num = num
#         print(min_num, end=" ")
#
#     elif min_num == deq[0]:
#         deq.popleft()
#         deq.append(num)
#
#         min_num = min(deq)
#         print(min_num, end=" ")
#
#     else:
#         deq.popleft()
#         deq.append(num)
#         if min_num > num: min_num = num
#         print(min_num, end=" ")
# --------------------------------------------------------------------------------------
import sys
from collections import deque

N_L = list(map(int , sys.stdin.readline().strip().split()))
arr = list(map(int , sys.stdin.readline().strip().split()))
deq = deque()

for i in range(N_L[0]):

    # arr[i]보다 큰 애들을 다 없앰.
    # arr[i] 앞에 있는 애들은 모두 arr[i]보다 작음.
    while deq and deq[-1][0] > arr[i]:
        deq.pop()

    deq.append((arr[i], i))

    # [i-L+1] ~ [i]
    # 오래된 값 제거
    if deq[0][1] <= i - N_L[1]:
        deq.popleft()

    print(deq[0][0], end=" ")