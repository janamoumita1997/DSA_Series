
nums = [0,1,1]
def contiguousArray(nums):
    cum_sum = 0
    prefix_sum = {}
    max_len = 0

    for i, num in enumerate(nums):

        cum_sum += -1 if num == 0 else 1

        if cum_sum == 0:
            max_len = i + 1
        elif cum_sum in prefix_sum:
            max_len = max(max_len, i - prefix_sum[cum_sum])
        else:
            prefix_sum[cum_sum] = i
    return max_len

print(contiguousArray(nums))