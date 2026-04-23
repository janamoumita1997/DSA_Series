"""
Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.

Return the shortest such subarray and output its length.

 

Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Example 2:

Input: nums = [1,2,3,4]
Output: 0

Example 3:

Input: nums = [1]
Output: 0

"""
nums = [2,6,4,8,10,9,15]
def find_window_sort(nums): 
    n = len(nums)
    l = 0
    r = n-1

    while l<n-1 and nums[l]<= nums[l+1]:
        l += 1
    if l == n-1:
        return 0
    while r>0 and nums[r] >= nums[r-1]:
        r -= 1
    max_val = max(nums[l:r+1])
    min_val = min(nums[l:r+1])

    while l>0 and nums[l-1]>min_val:
        l -= 1
    while r<n-1 and nums[r+1] < max_val:
        r +=1
    return r-l+1
print(find_window_sort(nums))