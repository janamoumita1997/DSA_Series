nums = [5,2,3,1,9,12,8]

def merge_sort(nums):
    if len(nums)<= 1:
        return nums
    mid = len(nums)//2
    left_side = merge_sort(nums[:mid])
    right_side = merge_sort(nums[mid:])
    return merge(left_side,right_side)

def merge(left_list:list,right_list:list) -> list:
    i,j = 0,0
    merged = []
    while i < len(left_list) and j < len(right_list):
        if left_list[i] <= right_list[j]:
            merged.append(left_list[i])
            i += 1
        else:
            merged.append(right_list[j])
            j += 1
    if i >= len(left_list) and j< len(right_list):
        merged.extend(right_list[j:])
    if i < len(left_list) and j >= len(right_list):
        merged.extend(left_list[i:])

    return merged

# left_list  = [2,3]
# right_list = [4,5,6]
# print(merge(left_list,right_list))
print(merge_sort(nums))