arr = [1, 2, 3, 5, 6, 7, 8, 10, 11, 15, 17, 18, 20]

low = 0
high = len(arr) - 1
key = 12

def interpolation_search(low, high, key):
    l = low
    r = high

    while l <= r and arr[key] >= low and arr[key] <= high:
        k = int(l + (r - l) * ((key - arr[l]) / (arr[r] - arr[l])))
        
        # 키가 없는 경우 반영해야됨
        if arr[k] == key:
            return k
        elif arr[k] > key:
            l = low
            r = k - 1
        else:
            l = k + 1
            r = high
    
    return None

res = interpolation_search(low, high, key)

if res or res == 0:
    print(res)
else:
    print(None)