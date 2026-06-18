from typing import List

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        
        count1 = [0] * 26
        count2 = [0] * 26
        
        # Build frequency map for s1 and the first window in s2
        for i in range(n1):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
        
        if count1 == count2:
            return True
        
        # Slide the window over s2
        for i in range(n1, n2):
            count2[ord(s2[i]) - ord('a')] += 1
            count2[ord(s2[i - n1]) - ord('a')] -= 1
            if count1 == count2:
                return True
        
        return False

# Example usage:
if __name__ == '__main__':
    sol = Solution()
    print(sol.checkInclusion("ab", "eidbaooo"))   # True
    print(sol.checkInclusion("ab", "eidboaoo"))    # False
    print(sol.checkInclusion("abc", "ccccbbbbaaaa")) # False
