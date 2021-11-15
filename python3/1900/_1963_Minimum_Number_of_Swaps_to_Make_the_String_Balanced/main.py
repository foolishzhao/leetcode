class Solution:
    def minSwaps(self, s: str) -> int:
        cnt, res = 0, 0
        for x in s:
            cnt += 1 if x == '[' else -1
            if cnt < 0:
                res += 1
                cnt += 2
        return res
