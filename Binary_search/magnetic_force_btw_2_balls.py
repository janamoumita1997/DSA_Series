def canPlace(pos,m,mid):
    count = 1
    last_pos = pos[0]

    for i in pos[1:]:
        if i - last_pos >= mid:
            count += 1
            last_pos = i
            if count == m:
                return True
    return False

def maxDistance(pos,m):
    pos.sort()
    left = 0
    right = pos[-1] - pos[0]
    res = 0

    while left <= right:
        mid = (left + right)//2
        if canPlace(pos, m, mid):
            res = mid
            left = mid + 1
        else:
            right = mid - 1
    return res

position = [1,2,3,4,7]
m = 3
print(maxDistance(position,m))
