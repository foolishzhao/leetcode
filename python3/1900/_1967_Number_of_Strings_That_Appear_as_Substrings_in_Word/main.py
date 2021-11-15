from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum([1 for x in patterns if x in word])
