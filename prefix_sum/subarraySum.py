"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
"""
nums = [1,-1,0]
k = 0

count = 0
n = len(nums)
for i in range(1,n):
    nums[i] += nums[i-1]

nums = [0] + nums
seen_list  = {0:0}
for i,val in enumerate(nums):
    if (val - k) in seen_list:
        count += 1
    seen_list[val] = i
print(count)

