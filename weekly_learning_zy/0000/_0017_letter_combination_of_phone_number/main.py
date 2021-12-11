from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(mapping[digits])
        prev = self.letterCombinations(digits[:-1])
        additional = mapping[digits[-1]]
        return [s + c for s in prev for c in additional]

    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(i, curres):
            if i == n:
                res.append(curres)
            for c in dict[digits[i]]:
                dfs(i + 1, curres + c)

        dict = {
            "2": "abc",
            "3": "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz",
        }
        if not digits:
            return []
        n = len(digits)
        res = []
        dfs(0, "")
        return res
if __name__ == '__main__':
    ans = Solution().letterCombinations("23")
    print(ans)