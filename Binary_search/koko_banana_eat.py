def minEatingSpeed(piles, h) :
    left = 1
    right = max(piles)
    res = right

    while left <= right:
        mid = (left + right)//2
        hours = 0
        for pile in piles:
            hours += (pile + mid - 1)// mid
        if hours <= h:
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    return res

piles = [3,6,7,11]
h = 8
print(minEatingSpeed(piles, h))