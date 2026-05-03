"""
You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.

 

Example 1:

Input: arr = [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: arr = [2,2,2]
Output: 0
Explanation: There is no mountain.
"""

arr = [2,2,2]

def find_longestmountain(nums):
    n = len(nums)
    if n <= 2:
        return 0
    i = 0
    j = 1
    k = 2
    max_len = 0
    while k<n:
        if nums[i] < nums[j] > nums[k]:
            l = i
            r = k
            while l > 0 and nums[l] > nums[l-1]:
                l -= 1
            while r < n-1 and nums[r] > nums[r+1]:
                r += 1
            max_len = max(max_len, r-l+1)
            i = r
            j = r+1
            k = r+2
        else:
            i += 1
            j += 1
            k += 1
    return max_len
    
print(find_longestmountain(arr))       

