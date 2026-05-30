nums = [0,1,2,4,2,1]
target = 3


class Solution:
    def find_peak(self, MountainArray):
        n = MountainArray.length() 
        left = 0
        right = n-1

        while left < right:
            mid = (left + right)//2
            if MountainArray.get(mid) < MountainArray.get(mid+1):
                left = mid+1
            else:
                right = mid
        return left

    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
    
        peak = self.find_peak(mountainArr)

        l1 = 0
        r1 = peak

        while l1 <= r1:
            mid = (l1 + r1) // 2
            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) < target:
                l1 = mid + 1
            else:
                r1 = mid -1
        
        l2 = peak + 1
        r2 = mountainArr.length()-1

        while l2 <= r2:
            mid = (l2 + r2) // 2
            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) < target:
                r2 = mid - 1
            else:
                l2 = mid + 1
        return -1
        