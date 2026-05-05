"""
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

nums = [-2,0,-1]
def maxProduct(nums):
    if not nums:
        return 0
    max_product = nums[0]
    min_product = nums[0]
    res = nums[0]
    for num in nums[1:]:
        if num < 0:
            min_product,max_product = max_product,min_product
        max_product = max(num, max_product*num)
        min_product = min(num, min_product*num)
        res = max(res, max_product)
    return res
print(maxProduct(nums))
