class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def check(u, v):
            lo, hi = (n // 2 - 1, n // 2) if n % 2 == 0 else (n // 2, n // 2)
            while lo >= 0 and v[lo] == v[hi]:
                lo -= 1
                hi += 1
            return u[:lo + 1] == v[hi:][::-1] or v[:lo + 1] == u[hi:][::-1]

        n = len(a)
        return check(a, b) or check(b, a)
