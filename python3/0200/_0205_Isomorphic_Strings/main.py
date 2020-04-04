class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        n = len(s)
        dt = dict()
        for i in range(n):
            sc, tc = s[i], t[i]
            if sc in dt:
                if dt[sc] != tc:
                    return False
            else:
                if tc in dt.values():
                    return False
                dt[sc] = tc

        return True
