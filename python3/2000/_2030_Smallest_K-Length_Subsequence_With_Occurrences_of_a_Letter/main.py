class Solution:
    def smallestSubsequence(self, s: str, k: int, l: str, r: int) -> str:
        quota, n = s.count(l) - r, len(s)
        st = list()

        for i, c in enumerate(s):
            while st and st[-1] > c and (len(st) + n - i > k) and (st[-1] != l or quota):
                if st.pop() == l:
                    quota -= 1
                    r += 1
            if len(st) < k:
                if c == l:
                    st.append(c)
                    r -= 1
                elif k - len(st) > r:
                    st.append(c)
        return ''.join(st)
