# 인덱스의 범위를 잘 조절하자. => 이 부분에서 대부분 에러가 발생함.
# and, or 같은 조건 연산자를 사용할 때, IndexError를 방지하고자 인덱싱이 붙는 조건은 뒤에 작성하자.

base_arr = [1, 3, 5, 2, 4, 3, 9, 6, 7, 8, 13, 11, 14, 15, 12]

def quick_sort(left, right):
    if left >= right:
        return None
    
    pivot = base_arr[left]
    
    l = left + 1
    r = right

    while l <= r:
        while l <= right and base_arr[l] <= pivot: l += 1
        while r > left and base_arr[r] >= pivot: r -= 1

        if l < r:
            base_arr[l], base_arr[r] = base_arr[r], base_arr[l]
    
    base_arr[r], base_arr[left] = base_arr[left], base_arr[r]

    quick_sort(left, r-1)
    quick_sort(r+1, right)


left = 0
right = len(base_arr) - 1
quick_sort(left, right)

print(base_arr)