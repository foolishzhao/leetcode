class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        s = "".join(S.split("-")).upper()
        if not s:
            return ""

        res, n = "", len(s)
        while n > 0:
            res = "-" + s[max(0, n - K): n] + res
            n -= K

        return res[1:] if res[0] == '-' else res
