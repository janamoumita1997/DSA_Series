s = "abb"

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        elif s[::-1] == s:
            return 1
        else:
            return 2
