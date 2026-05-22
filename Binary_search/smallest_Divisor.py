nums = [44,22,33,11,1]
threshold = 5

left = 1
right = max(nums)
res = right

while left<=right:
    mid = (left + right)//2

    divisor_sum = 0
    for i in nums:
        divisor_sum += (i + mid - 1)//mid

    if divisor_sum <= threshold:
        res = mid
        right = mid-1
    else:
        left = mid + 1
print(res)