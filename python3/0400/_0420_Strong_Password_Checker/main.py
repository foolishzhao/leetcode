class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        miss = 3
        if any('a' <= c <= 'z' for c in s):
            miss -= 1
        if any('A' <= c <= 'Z' for c in s):
            miss -= 1
        if any(c.isdigit() for c in s):
            miss -= 1

        n, i = len(s), 2
        replace, one, two = 0, 0, 0
        while i < n:
            if s[i] == s[i - 1] and s[i - 1] == s[i - 2]:
                curLen = 3
                while i + 1 < n and s[i + 1] == s[i]:
                    i += 1
                    curLen += 1

                replace += curLen // 3
                if curLen % 3 == 0:
                    one += 1
                elif curLen % 3 == 1:
                    two += 1
            i += 1

        if n < 6:
            return max(miss, 6 - n)
        elif n <= 20:
            return max(miss, replace)
        else:
            delete = n - 20
            replace -= min(delete, one)
            replace -= min(max(delete - one, 0) // 2, two)
            replace -= max(delete - one - 2 * two, 0) // 3

            return delete + max(miss, replace)
