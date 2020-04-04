from typing import Dict
from typing import Set
from typing import List


class Solution:
    # memorized dfs
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s or not wordDict:
            return []

        return self.dfs(s, set(wordDict), {})

    def dfs(self, s: str, wordDict: Set[str], dt: Dict[str, List[str]]) -> List[str]:
        if not s:
            return [""]

        # if using dt.get(s), will TLE
        if s in dt:
            return dt[s]

        res = []
        for i in range(len(s)):
            if s[:i + 1] in wordDict:
                curRes = self.dfs(s[i + 1:], wordDict, dt)
                for v in curRes:
                    if v:
                        res.append(s[:i + 1] + " " + v)
                    else:
                        res.append(s[:i + 1])

        dt[s] = res
        return res
