import copy

base_arr = [1, 3, 5, 2, 4, 3, 9, 6, 7, 8, 13, 11, 14, 15, 12]
copy_arr = copy.deepcopy(base_arr)

def merge_division(left, right):
    if left == right:
        return None
    
    mid = (left + right) // 2

    merge_division(left, mid)
    merge_division(mid+1, right)
    merge(left, mid, right)

def merge(left, mid, right):
    l = left
    r = mid + 1
    c = left

    while l <= mid and r <= right:
        if base_arr[l] < base_arr[r]:
            copy_arr[c] = base_arr[l]
            l += 1
            c += 1
        else:
            copy_arr[c] = base_arr[r]
            r += 1
            c += 1

    while l <= mid:
        copy_arr[c] = base_arr[l]
        c += 1
        l += 1

    while r <= right:
        copy_arr[c] = base_arr[r]
        c += 1
        r += 1

    base_arr[left:right+1] = copy_arr[left:right+1]

merge_division(0, len(base_arr)-1)
print(base_arr)