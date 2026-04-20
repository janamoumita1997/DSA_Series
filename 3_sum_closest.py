"""
Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

"""
def find_closest_sum(nums,target):
    nums.sort()
    n = len(nums)
    all_sum = []
    if len(nums) == 0:
        return "No solution"
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return min(abs(nums[0]-target),abs(nums[1]-target),abs(nums[0] + nums[1] -target))
    for i in range(n-2):
        if i>0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1,n-1
        while l<r:
            triplet_sum = nums[i] + nums[l] + nums[r]
            all_sum.append(triplet_sum)
            
            if triplet_sum == target:
                return triplet_sum
            elif triplet_sum<target:
                l += 1
            else:
                r -= 1
    min_diff = float("inf")
    min_sum = float("inf")            
    for i in all_sum:
        sum_diff = abs(i-target)
        if sum_diff < min_diff:
            min_sum = i

    return min_sum
nums = [0,0,0]
target = 1
print(find_closest_sum(nums,target))