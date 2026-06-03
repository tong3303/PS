import sys

input = sys.stdin.readline
n = int(input())
dice = []

for _ in range(n):
	temp = list(map(int, input().strip().split()))
	dice.append(temp)

re = [5, 3, 4, 1, 2, 0]
max_sum = 0


for i in range(6):  # i : 첫 dice의 밑면 번호
	bottom_value = dice[0][i]
	top_value = dice[0][re[i]]
	current_sum = 0

	# 0번 주사위 옆면 최댓값 탐색
	max_value = 0
	for dice_num in dice[0]:
		if dice_num != top_value and dice_num != bottom_value:
			max_value = max(max_value, dice_num) 
	
	current_sum += max_value

	# 1번 주사위 ~ n-1번 주사위 옆면 최댓값 찾기
	for j in range(1, n):
		bottom_idx = dice[j].index(top_value)
		bottom_value = dice[j][bottom_idx]
		top_value = dice[j][re[bottom_idx]]

		max_value = 0
		for dice_num in dice[j]:
			if dice_num != top_value and dice_num != bottom_value:
				max_value = max(max_value, dice_num)

		current_sum += max_value

	max_sum = max(max_sum, current_sum)
print(max_sum)