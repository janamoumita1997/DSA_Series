nums = [0,0,1,2,3,3]

def remove_duplicates(nums):

    if len(nums) < 3:
        return len(nums)
    k = 2
    for i in range(2,len(nums)):
        if nums[i] != nums[k-2]:
            nums[k] = nums[i]
            k += 1
    return k

print(remove_duplicates(nums))