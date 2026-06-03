arr = [1, 3, 8, 13, 13, 16, 21, 26, 27, 30, 33, 36, 39, 41, 44, 49]

key = 30
low = 0
high = len(arr) - 1
result = 0

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        result = mid
        break
    
    elif arr[mid] < key:
        low = mid + 1
    
    else:
        high = mid - 1

if result:
    print(f"{key}의 자리는 {result}입니다")
else:
    print(f"{key}는 arr에 존재하지 않음.")