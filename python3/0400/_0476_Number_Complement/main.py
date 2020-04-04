class Solution:
    def findComplement(self, num: int) -> int:
        mask = 1
        while (num & mask) != num:
            mask = (mask << 1) | 1

        return num ^ mask
