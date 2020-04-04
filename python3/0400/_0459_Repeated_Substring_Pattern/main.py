class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # s can be 3 * 3, s' length can be odd or even
        if not s:
            return False

        n = len(s)
        l = n // 2
        while l > 0:
            if not n % l and s[:l] * (n // l) == s:
                return True
            l -= 1

        return False

    """
    Let's say T = S + S.
    `S is Repeated => From T[1:-1] can find S` is obvious.
    
    If from T[1:-1] we found S at index p-1, which is index p in T and S.
    Let s1 = S[:p], S can be represented as s1X1. 
    
    Then S = X1s1 = s1X1 (1).
    len(X1) < p is false because if so we should find S in T[1:-1] at index len(X1) rather than p.
    len(X1) == p => X1 = s1 => S is Repeated.
    len(X1) > p => X1 has prefix s1 so can be represented as s1X2.
    X1 = s1X2 => s1X2s1= s1s1X2 => X2s1 = s1X2.
    len(X2) < p is false because if so S = X2s1s1 = s1s1X2 and we should find S at index len(X2) rather than p.
    
    As long as len(Xi-1) > p, we can get Xis1 = s1Xi through the prefix step and prove len(Xi) < p is false. 
    Eventually we can get a Xn, len(Xn) == p and Xn = s1 => S is Repeated.
    """

    def repeatedSubstringPattern2(self, s: str) -> bool:
        return s in (s + s)[1:-1]
