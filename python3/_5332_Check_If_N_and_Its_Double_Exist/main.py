from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        st = set(arr)
        zeroCount = arr.count(0)
        for x in arr:
            if not x and zeroCount >= 2:
                return True

            if x and x * 2 in st:
                return True

        return False


if __name__ == '__main__':
    Solution().checkIfExist([-2, 0, 10, -19, 4, 6, -8])
