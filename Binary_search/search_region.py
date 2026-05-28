nums = [5,6,6,6,6,7,7,7,8,8,8,8,8,9,10]
target = 6

# find first location
left = 0
right = len(nums) - 1

res = [-1,-1]

while left <= right:
    mid = (left + right)//2
    if nums[mid] == target:
        res[0] = mid
        right = mid - 1
    elif nums[mid] < target:
        left = mid+1
    else:
        right = mid - 1

left = 0
right = len(nums) - 1
while left <= right:
    mid = (left + right)//2
    if nums[mid] == target:
        res[1] = mid
        left = mid + 1
    elif nums[mid] < target:
        left = mid+1
    else:
        right = mid - 1

print(res)