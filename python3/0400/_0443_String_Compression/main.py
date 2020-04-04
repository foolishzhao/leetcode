from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        n, i, k = len(chars), 0, 0
        while i < n:
            j = i + 1
            while j < n and chars[j] == chars[i]:
                j += 1

            chars[k] = chars[i]
            if j - i == 1:
                k += 1
            elif j - i == 2:
                chars[k + 1] = '2'
                k += 2
            else:
                k += 1
                for v in str(j - i):
                    chars[k] = v
                    k += 1
            i = j

        return k
