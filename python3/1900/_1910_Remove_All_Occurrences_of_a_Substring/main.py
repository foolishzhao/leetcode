class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        st, n = list(), len(part)
        for c in s:
            st.append(c)
            if len(st) >= n and ''.join(st[-n:]) == part:
                for _ in range(n):
                    st.pop()
        return ''.join(st)
