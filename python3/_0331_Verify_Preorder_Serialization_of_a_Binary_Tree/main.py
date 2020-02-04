class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        st = list()
        for c in preorder.split(","):
            st.append(c)
            while len(st) >= 2 and st[-1] == '#' and st[-2] == '#':
                st.pop()
                st.pop()
                if not st:
                    return False
                st[-1] = '#'

        return len(st) == 1 and st[0] == '#'
