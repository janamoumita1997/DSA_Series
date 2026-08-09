class Solution:
    def getSum(self, a: int, b: int) -> int:
        masking = 0xFFFFFFFF
        while b != 0:
            carry = (a & b) << 1
            a = (a^b) & masking
            b = carry & masking
        return a if a <= 0x7FFFFFFF else ~(a ^ masking)