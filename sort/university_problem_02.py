import sys


input = sys.stdin.readline


while True:
	# player 입력받고, player 순서 리스트로 반환
	player = input().strip()
	if player == '#': break

	tmp_list = ['S', 'E', 'N', 'W']
	player_order = []

	tmp_idx = tmp_list.index(player) - 1
	for _ in range(4):
		player_order.append(tmp_list[tmp_idx])
		tmp_idx -= 1


	# 카드 입력 받고 리스트로 변환
	card = ''
	for _ in range(2):
		card += input().strip()
		

	card_list = [card[i:i+2] for i in range(0, len(card), 2)]
	# card_list에 있는 데이터를 player_card에 집어 넣기
	player_card = {
		'S': [],
		'W': [],
		'N': [],
		'E': []
	}


	# 정렬 우선순위
	first_value = {'C' : 0, 'D': 1, 'S':2, 'H':3}
	second_value = {k: i for i, k in enumerate('23456789TJQKA')}

	card_type = ['C', 'D', 'S', 'H']
	i = 0

	for card in card_list:
		given_people = player_order[i]
		player_card[given_people].append(card)
		i = (i + 1) % 4

	for t in player_card.keys():
		player_card[t].sort(key = lambda x: (first_value[x[0]], second_value[x[1]]))

	for p, c_li in player_card.items():
		print(p, ":", end=" ")
		for c in c_li:
			print(c, end=" ")
		print()