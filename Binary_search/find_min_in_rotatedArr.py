nums = [4,5,6,7,1,4]
def find_min_in_rotated_arr(nums):
    left = 0
    right = len(nums)-1

    while left < right:
        mid = (left + right)//2
        if nums[mid] < nums[mid+1]:
            left = mid + 1
        else:
            right = mid

    if left == len(nums)-1:
        return nums[0]
    else:
        return nums[left+1]
print(find_min_in_rotated_arr(nums))