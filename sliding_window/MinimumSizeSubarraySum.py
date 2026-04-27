""""
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""
arr = [1,4,4]
target = 4

n = len(arr)
l = 0
current_sum = 0
count = float('inf')
for r in range(n):
    current_sum += arr[r]
    while current_sum >= target:
        count = min(count,r-l+1)
        current_sum -= arr[l]
        l += 1
res = count if count != float("inf") else 0
print(res)
