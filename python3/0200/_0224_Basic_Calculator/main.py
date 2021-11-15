class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        st, cur, num, sign = list(), 0, 0, 1
        for c in s + '+':
            if c == '(':
                st.append(cur)
                st.append(sign)
                cur, sign = 0, 1
            elif c == ')':
                cur += sign * num
                num = cur
                sign = st.pop()
                cur = st.pop()
            elif c == '+':
                cur += sign * num
                num, sign = 0, 1
            elif c == '-':
                cur += sign * num
                num, sign = 0, -1
            elif c.isdigit():
                num = num * 10 + int(c)
        return cur
