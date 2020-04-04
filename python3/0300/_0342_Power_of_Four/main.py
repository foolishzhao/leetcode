class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and (num & (num - 1)) == 0 and (0x55555555 & num) > 0
