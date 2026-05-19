"""


"""

weights = [1,2,3,4,5,6,7,8,9,10]
days_ = 5
def shipWithinDays(weights,days_):
    left = max(weights)
    right = sum(weights)
    while left < right:
        mid = (left + right)//2
        day_count = 1
        current_load = 0
        for weight in weights:
            if current_load + weight > mid:
                day_count += 1
                current_load = 0
            current_load += weight
        if day_count == days_:
            return mid
        elif day_count < days_:
            right = mid
        else:
            left = mid+1
    return left

print(shipWithinDays(weights,days_))