class Solution:
    def simplifyPath(self, path: str) -> str:
        st = list()
        for p in path.split('/'):
            if p == '.' or p == '':
                continue
            elif p == '..':
                if st:
                    st.pop()
            else:
                st.append(p)
        return '/' + '/'.join(st)
