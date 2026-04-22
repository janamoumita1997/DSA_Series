"""
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"

Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"

"""
from typing import List
from functools import cmp_to_key

nums = [3,30,34,5,9]
def find_largest(nums):
    str_nums = list(map(str, nums))

    # Define a comparator that decides order based on the concatenation result
    def compare(x: str, y: str) -> int:
        if x + y > y + x:
            return -1
        elif x + y < y + x:
            return 1
        else:
            return 0

    # Sort the numbers using the custom comparator
    str_nums.sort(key=cmp_to_key(compare))

    # Join the sorted numbers to form the largest number
    result = ''.join(str_nums)

    # If the largest number is '0' (i.e., multiple zeroes), return '0'
    return '0' if result[0] == '0' else result
print(find_largest(nums))