from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = list()
        for t in tokens:
            if t == '+':
                st.append(st.pop() + st.pop())
            elif t == '-':
                st.append(-st.pop() + st.pop())
            elif t == '*':
                st.append(st.pop() * st.pop())
            elif t == '/':
                op1 = st.pop()
                # int (u  / v): truncate toward zero
                # If x is floating point, the int conversion truncates towards zero.
                st.append(int(st.pop() / op1))
            else:
                st.append(int(t))
        return st.pop()
