arr = [0,1,0]

def find_peak(arr):
    n = len(arr)
    if n <= 2:
        return -1
    
    left = 0
    right = n - 1

    while left < right:
        mid = (left + right)//2
        if arr[mid] < arr[mid+1]:
            left = mid + 1
        else:
            right = mid
    return left