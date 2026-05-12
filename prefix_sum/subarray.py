"""
Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1], k = 1
Output: 1
Example 2:

Input: nums = [1,2], k = 4
Output: -1
Example 3:

Input: nums = [2,-1,2], k = 3
Output: 3
"""
from typing import List
from collections import deque

def shortestSubarray(nums: List[int], k: int) -> int:
    n = len(nums)
    P = [0] * (n+1)
    for i in range(n):
        P[i+1] = P[i] + nums[i]
    result = n+1
    dq = deque()
    for i,curr in enumerate(P):
        while dq and curr - P[dq[0]] >= k:
            result = min(result, i-dq[0])
            dq.popleft()
        while dq and curr <= P[dq[-1]]:
            dq.pop()
        dq.append(i)
    return result if result < n+1 else -1

nums = [84,-37,32,40,95]
k = 168

print(shortestSubarray(nums,k))

