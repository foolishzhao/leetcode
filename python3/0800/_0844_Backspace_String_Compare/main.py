class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(x):
            st = list()
            for c in x:
                if c == '#':
                    if st:
                        st.pop()
                else:
                    st.append(c)
            return ''.join(st)

        return helper(s) == helper(t)

    def backspaceCompare2(self, s: str, t: str) -> bool:
        def helper(x):
            res, skip = "", 0
            for c in x[::-1]:
                if c == '#':
                    skip += 1
                else:
                    if skip:
                        skip -= 1
                    else:
                        res += c
            return res[::-1]

        return helper(s) == helper(t)
