class Solution:
    def lengthLongestPath(self, input: str) -> int:
        res, st = 0, [0]
        for s in input.split('\n'):
            i = 0
            while i < len(s) and s[i] == '\t':
                i += 1

            level = i + 1
            while len(st) > level:
                st.pop()

            curLen = st[-1] + len(s) - level + 1
            st.append(curLen)
            if '.' in s:
                res = max(res, curLen + level - 1)

        return res


if __name__ == '__main__':
    Solution().lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")
