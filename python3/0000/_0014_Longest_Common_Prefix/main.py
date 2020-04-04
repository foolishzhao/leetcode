from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        if len(strs):
            for i in range(len(strs[0])):
                for s in strs:
                    if i == len(s):
                        return res
                    elif s[i] != strs[0][i]:
                        return res
                res += strs[0][i]

        return res
