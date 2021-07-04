class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        st, cur = set(), ''
        for w in (word + 'a'):
            if w.isdigit():
                cur += w
            else:
                if cur:
                    st.add(int(cur))
                    cur = ''
        return len(st)
