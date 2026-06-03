arr = [5, 3, 8, 4, 9, 1, 6, 2, 7]

low = 0
high = len(arr) - 1
user = 3
k = user - 1

def quick_search(low, high, k):
    if low > high:
        return None
    
    pivot = arr[low]
    pi_idx = low

    l = low + 1
    r = high
    
    while l <= r:
        while l <= high and arr[l] <= pivot: l += 1
        while r > low and arr[r] >= pivot: r -= 1

        if l <= r:
            arr[l], arr[r] = arr[r], arr[l]
    
    arr[r], arr[pi_idx] = arr[pi_idx], arr[r]
    pi_idx = r

    if pi_idx == k:
        return pivot
    elif pi_idx > k:
        return quick_search(0, pi_idx-1, k)
    else:
        return quick_search(pi_idx+1, len(arr)-1, k)
    
res = quick_search(low, high, k)
if res or res == 0:
    print(res)