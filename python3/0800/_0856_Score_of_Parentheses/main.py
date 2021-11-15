class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st, cur = list(), 0
        for x in s:
            if x == '(':
                st.append(cur)
                cur = 0
            else:
                cur = 1 if not cur else cur * 2
                cur += st.pop()
        return cur

    def scoreOfParentheses2(self, s: str) -> int:
        res, l = 0, 0
        for i in range(len(s)):
            l += 1 if s[i] == '(' else -1
            if s[i] == ')' and s[i - 1] == '(':
                res += 1 << l
        return res
