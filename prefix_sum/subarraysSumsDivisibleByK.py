from typing import List

def subarraysDivByK(nums: List[int], k: int) -> int:
    reminder_lst = {0:1}
    prefix_sum = 0
    count = 0

    for num in nums:
        prefix_sum += num
        reminder = prefix_sum % k
        count += reminder_lst.get(reminder,0)

        reminder_lst[reminder] = reminder_lst.get(reminder,0) + 1
    return count
nums = [4,5,0,-2,-3,1]
k = 5
print(subarraysDivByK(nums, k))