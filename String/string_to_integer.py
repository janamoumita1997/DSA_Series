''' Python Code with type hints '''

from typing import List

class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        i, n = 0, len(s)

        # Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1

        if i == n:
            return 0

        # Check sign
        sign = 1
        if s[i] == '+' or s[i] == '-':
            sign = -1 if s[i] == '-' else 1
            i += 1

        result = 0
        # Build the number
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            result = result * 10 + digit
            i += 1

        return sign * result

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.myAtoi("42"))              # Output: 42
    print(sol.myAtoi("   -42"))          # Output: -42
    print(sol.myAtoi("4193 with words")) # Output: 4193
