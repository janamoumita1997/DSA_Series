"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
class Solution:
    def maxConsecutiveOnes(self,nums : list[int],k: int) -> int:
        n = len(nums)
        zero_count = {0:0}
        l = 0
        max_count = 0

        for r in range(n):
            if nums[r] == 0:
                zero_count[0] = zero_count.get(0,0) + 1
            while zero_count[0] > k:
                if nums[l] == 0:
                    zero_count[0] -= 1
                l += 1
            max_count = max(max_count,r-l+1)
        return max_count
    
# print(Solution().maxConsecutiveOnes(nums,k))


# count only consecutive ones
nums = [1,1,0,1,1,0]
n = len(nums)
max_count = 0
l = 0

for r in range(n):
    while nums[r] == 0 and l <= r:
        l += 1
    max_count = max(max_count, r-l+1)
print(max_count)
