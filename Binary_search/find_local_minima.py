nums = [9, 6, 3, 14, 5, 7, 4]

n = len(nums)
left = 0
right = n-1
res = -1

while left <= right:
    mid = (left + right)//2
    if (mid==0 or nums[mid]< nums[mid-1]) and (mid == n-1 or nums[mid] < nums[mid+1]):
        res = mid
        right = mid-1
    elif mid>0 and nums[mid-1] < nums[mid]:
        right = mid-1
    else:
        left = mid+1
print(res)

