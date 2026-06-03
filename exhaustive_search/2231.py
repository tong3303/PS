import sys

n = int(sys.stdin.readline())

div_sum = 0  # 분해합을 저장할 변수

# n부터 -1씩 내려오면서 분해합을 검수
for i in range(n-1, 0, -1):
    tmp_sum = i + sum([int(s_n) for s_n in str(i)])  # 분해합 구하기
    if tmp_sum == n:  # i의 분해합이 n이면 div_sum에 저장
        div_sum = i

    # i의 일의 자리가 9면서 분해합보다 작으면 현재 i가 최솟값 => 십, 백, 천 ..... 자리도 고려해야됨.
    # if str(i)[-1] == '9' and tmp_sum <= n:
    #     break

print(div_sum)
