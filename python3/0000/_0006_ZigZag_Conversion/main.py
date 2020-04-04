class Solution:
    def convert(self, s: str, numRows: int) -> str:
        sArr = [""] * numRows
        n, i = len(s), 0
        while i < n:
            j = 0
            while j < numRows and i < n:
                sArr[j] += s[i]
                i += 1
                j += 1

            j = numRows - 2
            while j > 0 and i < n:
                sArr[j] += s[i]
                j -= 1
                i += 1

        return "".join(sArr)


if __name__ == '__main__':
    Solution().convert("PAYPALISHIRING", 3)
