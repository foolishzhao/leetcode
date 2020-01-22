class Solution:
    def freqAlphabets(self, s: str) -> str:
        dt = {str(i) if i <= 9 else str(i) + '#': chr(ord('a') + i - 1) for i in range(1, 27)}

        res = ""
        i, j, n = 0, 0, len(s)
        while j < n:
            if s[j] == '#':
                while i < j - 2:
                    res += dt[s[i]]
                    i += 1
                res += dt[s[j - 2:j + 1]]
                i += 3

            j += 1

        while i < n:
            res += dt[s[i]]
            i += 1

        return res
