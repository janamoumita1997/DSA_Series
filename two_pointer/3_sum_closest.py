def threeSumClosest(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n-2):
            left = i+1
            right = n-1
            while left<right:
                total = nums[i] + nums[left] + nums[right]
                res.append(total)
                if total == target:
                    return total
                elif total<target:
                    left += 1
                else:
                    right -= 1  

        min_val = float('inf')
        closet_sum = float('inf')  
        for i in res:
            if abs(i-target)<min_val:
                min_val = abs(i-target)
                closet_sum = i
        return closet_sum