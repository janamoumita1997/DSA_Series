arr = [87, 93, 51, 81, 68, 99, 59]
k = 4

def can_allocate(arr,k,mid):
    count = 1
    last_pos = min(arr)
    for i in range(1, len(arr)):
        if (arr[i] - last_pos) >= mid:
            count += 1
            last_pos = arr[i] 
            if count == k:
                return True
    return False


def max_distance(arr,k):

    if len(arr) < k:
        return 0
    
    arr.sort()
    left = 0
    right = max(arr)
    res = 0

    while left <= right:
        mid = (left + right)//2
        if can_allocate(arr, k, mid):
            res = mid
            left = mid + 1
        else:
            right = mid - 1
    return res

print(max_distance(arr,k))
