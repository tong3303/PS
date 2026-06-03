import sys

str = sys.stdin.readline().strip()
stack = []
slice_bar = 0
is_prior_open = True

for s in str:
    if s == "(":
        stack.append(s)
        slice_bar += 1
        is_prior_open = True

    # 레이저인 경우
    elif s == ")" and is_prior_open:
        slice_bar -= 1
        stack.pop()
        slice_bar += len(stack)
        is_prior_open = False

    # 막대기 종료
    else:
        stack.pop()
        is_prior_open = False

print(slice_bar)

