from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        self.dfs(res, "", digits, 0)

        return res

    def dfs(self, res: List[str], oneRes: str, digits: str, pos: int):
        if pos == len(digits):
            res.append(oneRes)
            return

        dt = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz",
        }

        digit = digits[pos]
        for c in dt.get(digit):
            self.dfs(res, oneRes + c, digits, pos + 1)
