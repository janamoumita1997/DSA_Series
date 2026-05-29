nums = [1,1,2,3,3,4,4,8,8]

n = len(nums)
if n%2 == 0:
    print(-1)

left = 0
right = n

while left < right:
    mid = (left +right)//2
    
    if mid%2 == 1:
        mid -= 1
    
    
    if nums[mid] == nums[mid+1]:
        left = mid + 2
    else:
        right = mid
        
print(nums[left])

