nums = [9, 6, 3, 14, 5, 7, 4]

n = len(nums)
left = 0
right = n-1

while left < right:
    mid = (left + right)//2
    if nums[mid] < nums[mid+1]:
        left = mid+1
    else:
        right = mid
print(left)

l1,r1 = 0,left
while l1<r1:
    mid = (l1 + r1)//2
    if nums[mid] > nums[mid+1]:
        l1 = mid + 1
    else:
        r1 = mid
print(l1)