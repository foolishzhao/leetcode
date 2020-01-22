import string


class Solution:
    """
    If we think of A..Z as base-26 number,
    0-based index is A -> 0, ..., Z -> 25,
    1-based index is A -> 1, ..., Z -> 26,
    Given n is 1-based index, n - 1 means changing from 1-based index to 0-based index.
    0-based index is more natural for mod and divide, because x mod 26 return [0, 25]
    """

    def convertToTitle(self, n: int) -> str:
        if not n:
            return ""

        cur = (n - 1) % 26
        n = (n - 1) // 26

        return self.convertToTitle(n) + string.ascii_uppercase[cur]

    def convertToTitle2(self, n: int) -> str:
        res = ""
        while n:
            res = string.ascii_uppercase[(n - 1) % 26] + res
            n = (n - 1) // 26

        return res
