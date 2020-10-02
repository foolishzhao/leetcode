from typing import List
import collections


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(key=lambda x: len(x), reverse=True)
        st = set()
        i = 0
        for j, s in enumerate(strs + [""]):
            if len(s) != len(strs[i]):
                counter = collections.Counter(strs[i: j])
                for ss, cnt in counter.items():
                    if cnt == 1:
                        if all([not self.isSubsequence(p, ss) for p in st]):
                            return len(ss)
                for ss in counter:
                    st.add(ss)
                i = j
        return -1

    def isSubsequence(self, p, s):
        pLen, sLen = len(p), len(s)
        dp = [[False] * (sLen + 1) for _ in range(pLen + 1)]
        dp[0][0] = True
        for i in range(1, pLen + 1):
            dp[i][0] = True
            for j in range(1, sLen + 1):
                dp[i][j] = dp[i - 1][j]
                if p[i - 1] == s[j - 1]:
                    dp[i][j] |= dp[i - 1][j - 1]
        return dp[-1][-1]

    def isSubsequence2(self, p, s):
        i = 0
        for c in p:
            if i < len(s) and c == s[i]:
                i += 1
        return i == len(s)
