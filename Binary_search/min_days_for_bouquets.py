bloomday = [7,7,7,7,12,7,7]
m = 2
k = 3

# def count_bouquets(bloomday,days,k):
#     garden = [i if i <= days else 0 for i in bloomday]
#     left = 0
#     right = left + k
#     count = 0

#     while right <= len(garden):
#         if all(garden[left:right]):
#             count += 1
#             left = right
#         else:
#             left += 1
#         right = left + k
#     return count
def count_bouquets(bloomday,days,k):
    count = 0
    flower = 0

    for bloom in bloomday:
        if bloom >= days:
            flower += 1
        else:
            flower = 0

        if flower == k:
            count += 1
            flower = 0
    return count
    

def min_days(bloomday,m,k):
    low = min(bloomday)
    high = max(bloomday)
    res = high
    if len(bloomday) < m*k:
        return -1
    while low <= high:
        mid = (low + high)//2
        bouquets_nums = count_bouquets(bloomday,mid,k)
        if bouquets_nums < m:
            low = mid + 1
        else:
            res = mid
            high = mid-1
    return res
            

print(min_days(bloomday,m,k))
