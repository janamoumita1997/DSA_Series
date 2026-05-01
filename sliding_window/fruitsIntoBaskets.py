class Solution:
    def main(self,nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        l = 0
        max_count = 1
        fruit_count = {nums[l]:1}
        for r in range(1,n):
            fruit_count[nums[r]] = fruit_count.get(nums[r],0) + 1       
            while len(fruit_count) > 2:
                fruit_count[nums[l]] = fruit_count.get(nums[l]) - 1 
                if fruit_count[nums[l]] == 0:
                    del fruit_count[nums[l]]
                l += 1
            max_count = max(max_count, r-l+1)
        return max_count


nums = [5,5,4,4,4,4,1,2,2,2,4]
print(Solution().main(nums))