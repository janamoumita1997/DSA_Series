"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

"""
nums = []
def find_square_of_soted_ar(nums):
    n = len(nums)
    if n == 1:
        return [nums[0]**2]
    l = 0
    r = n-1
    while l<r:
        if abs(nums[r]) >= abs(nums[l]):
            nums[r] = nums[r]**2
            
        else:
            temp = nums[r]
            nums[r] = nums[l]**2
            nums[l] = temp
        r -= 1
    return nums
print(find_square_of_soted_ar(nums))