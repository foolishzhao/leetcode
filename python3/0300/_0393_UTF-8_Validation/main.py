from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        data = [x & 0xff for x in data]

        i, n = 0, len(data)
        while i < n:
            cur = data[i]
            if cur >> 7 == 0:
                i += 1
            elif cur >> 5 == 6:
                if i + 1 < n and (data[i + 1] >> 6) == 2:
                    i += 2
                else:
                    return False
            elif cur >> 4 == 14:
                if i + 2 < n and (data[i + 1] >> 6) == 2 and (data[i + 2] >> 6) == 2:
                    i += 3
                else:
                    return False
            elif cur >> 3 == 30:
                if i + 3 < n and (data[i + 1] >> 6) == 2 and (data[i + 2] >> 6) == 2 and (data[i + 3] >> 6) == 2:
                    i += 4
                else:
                    return False
            else:
                return False

        return True

    def validUtf82(self, data: List[int]) -> bool:
        data = [x & 0xff for x in data]
        count = 0
        for d in data:
            if count:
                if d >> 6 != 0b10:
                    return False
                count -= 1
            else:
                if d >> 7 == 0:
                    continue
                elif d >> 5 == 0b110:
                    count = 1
                elif d >> 4 == 0b1110:
                    count = 2
                elif d >> 3 == 0b11110:
                    count = 3
                else:
                    return False

        return not count
