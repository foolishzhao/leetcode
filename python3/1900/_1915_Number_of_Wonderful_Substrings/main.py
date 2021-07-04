class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        cnt = [1] + [0] * 1023
        res, cur = 0, 0
        for c in word:
            cur ^= 1 << (ord(c) - ord('a'))
            res += cnt[cur]
            for i in range(10):
                res += cnt[cur ^ (1 << i)]
            cnt[cur] += 1

        return res
