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
# nums = [1,-1,0]
# k = 0

# count = 0
# n = len(nums)
# for i in range(1,n):
#     nums[i] += nums[i-1]

# nums = [0] + nums
# seen_list  = {0:1}
# for i,val in enumerate(nums):
#     if (val - k) in seen_list:
#         count += 1
#     seen_list[val] = seen_list.get(val,0) + 1
# print(count)



nums = [1,-1,0]
k = 0

count = 0
prefix_sum = {0:1}
current_sum = 0

for num in nums:
    current_sum += num
    if current_sum - k in prefix_sum:
        count += prefix_sum[current_sum - k]
    prefix_sum[current_sum] = prefix_sum.get(current_sum,0) + 1
print(count)
