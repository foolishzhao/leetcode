class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText) // rows
        c, res = 0, ''
        while c < cols:
            i, j = 0, c
            while i < rows and j < cols:
                # mat[i][j] = encodedText[i * cols + j]
                res += encodedText[i * cols + j]
                i += 1
                j += 1
            c += 1
        return res.rstrip()
