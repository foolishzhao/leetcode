from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        res, i, dt = '', 0, dict(knowledge)
        while i < len(s):
            if s[i] == '(':
                j = i + 1
                while s[j] != ')':
                    j += 1

                res += dt.get(s[i + 1: j], '?')
                i = j
            else:
                res += s[i]
            i += 1
        return res
