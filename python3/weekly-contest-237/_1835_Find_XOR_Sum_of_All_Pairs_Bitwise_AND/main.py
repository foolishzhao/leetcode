from typing import List
import operator
from functools import reduce


class Solution:
    # (a1^a2) & (b1^b2) = (a1&b1) ^ (a1&b2) ^ (a2&b1) ^ (a2&b2)
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        return reduce(operator.xor, arr1) & reduce(operator.xor, arr2)
