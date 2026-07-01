nums = [-1,0,3,5,9,12]
target = 9

# using binary search
def binary_search(nums,target):
    left = 0
    right = len(nums)-1

    while left <= right:
        mid = (left + right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid -1
    return -1
# print(binary_search(nums,target))

# using recursion
def binary_search(nums,target,left,right):
    if left >right:
        return -1
    mid = (left+right)//2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search(nums,target,mid+1,right)
    else:
        return binary_search(nums,target,left,mid-1)
    
print(binary_search(nums,target,0, len(nums)-1))