class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if n == k:
            return "0"

        st = list()
        for d in num:
            while st and k and st[-1] > d:
                st.pop()
                k -= 1

            st.append(d)

        while st and k:
            st.pop()
            k -= 1

        res = ''.join(st).lstrip('0')
        return res if res else '0'
