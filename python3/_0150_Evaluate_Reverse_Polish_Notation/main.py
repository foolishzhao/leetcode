from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0

        op = {'+', '-', '*', '/'}
        st = []
        for token in tokens:
            if token in op:
                u = st.pop()
                v = st.pop()
                if token == '+':
                    st.append(v + u)
                elif token == '-':
                    st.append(v - u)
                elif token == '*':
                    st.append(v * u)
                else:
                    # can use v // u, int(v / u) can truncate to zero
                    st.append(int(v / u))
            else:
                st.append(int(token))

        return st.pop()
