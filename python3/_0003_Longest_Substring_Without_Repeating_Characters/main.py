class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None:
            return 0

        st = set()
        i, res = 0, 0
        for j, v in enumerate(s):
            if v in st:
                res = max(res, j - i)
                while s[i] != v:
                    st.remove(s[i])
                    i += 1
                i += 1
            else:
                st.add(v)

        return max(res, len(s) - i)

    def lengthOfLongestSubstring2(self, s: str) -> int:
        if s is None:
            return 0

        i, res = 0, 0
        dt = {}
        for j, v in enumerate(s):
            if v in dt and dt.get(v) >= i:
                res = max(res, j - i)
                i = dt.get(v) + 1
            dt[v] = j

        return max(res, len(s) - i)


if __name__ == '__main__':
    Solution().lengthOfLongestSubstring("tmmzuxt")
