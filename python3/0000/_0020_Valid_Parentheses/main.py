class Solution:
    def isValid(self, s: str) -> bool:
        st = list()
        dt = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for c in s:
            if c in dt:
                st.append(dt[c])
            else:
                if not st or st[-1] != c:
                    return False
                st.pop()
        return not st
