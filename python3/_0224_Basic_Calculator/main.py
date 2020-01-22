class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        st = list()
        res, num, sign = 0, 0, 1
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '+':
                res += sign * num
                num = 0
                sign = 1
            elif c == '-':
                res += sign * num
                num = 0
                sign = -1
            elif c == '(':
                st.append(res)
                st.append(sign)

                res = 0
                sign = 1
            elif c == ')':
                res += sign * num
                num = 0

                res *= st.pop()
                res += st.pop()

        if num:
            res += sign * num

        return res
