class Solution:
    def isValid(self, s: str) -> bool:
        dt = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        st = []
        for c in s:
            if c in dt.values():
                st.append(c)
            elif c in dt.keys():
                if not st or dt[c] != st.pop():
                    return False
            else:
                return False

        return not st
