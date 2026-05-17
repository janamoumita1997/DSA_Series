n = 100

def arrangeCoins(n):
    left,right = 1, n
    mid = 0

    while left<=right:
        mid = (left + right) // 2
        coin_cap = (mid*(mid+1))//2
        if coin_cap == n:
            return mid
        elif coin_cap > n:
            right = mid -1
        else:
            left = mid + 1

    coin_cap = (mid*(mid+1))//2
    if coin_cap < n:
        return mid
    else:
        return mid -1
print(arrangeCoins(n))