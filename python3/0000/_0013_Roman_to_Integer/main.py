class Solution:
    def romanToInt(self, s: str) -> int:
        dt = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        res = 0
        for i, v in enumerate(s):
            if i == len(s) - 1 or dt[v] >= dt[s[i + 1]]:
                res += dt[v]
            else:
                res -= dt[v]

        return res
