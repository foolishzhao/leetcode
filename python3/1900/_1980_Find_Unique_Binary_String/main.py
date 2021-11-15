from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        st, n = set(nums), len(nums[0])
        for i in range(2 ** n):
            t = bin(i)[2:]
            t = '0' * (n - len(t)) + t
            if t not in st:
                return t

    def findDifferentBinaryString2(self, nums: List[str]) -> str:
        return ''.join(str(1 - int(num[i])) for i, num in enumerate(nums))
