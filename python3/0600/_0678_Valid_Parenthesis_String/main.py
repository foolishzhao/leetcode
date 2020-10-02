class Solution:

    # lmax means the maximum number of unbalanced '(' that COULD be paired.
    # lmax considers each '*' as '(', which should never be negative

    # lmin means the number of unbalanced '(' that MUST be paired
    # lmin considers each '*' as ')' as much as possible (treat '*' as empty string if lmin == 0).

    # In the end, lmin should be 0.
    # If it's larger than 0, it means even if we consider every '*' as ')', there is still some '(' left.
    def checkValidString(self, s: str) -> bool:
        lmin, lmax = 0, 0
        for c in s:
            if c == '(':
                lmax += 1
                lmin += 1
            elif c == ')':
                lmax -= 1
                lmin = max(lmin - 1, 0)
            else:
                lmax += 1
                lmin = max(lmin - 1, 0)
            if lmax < 0:
                return False
        return lmin == 0
