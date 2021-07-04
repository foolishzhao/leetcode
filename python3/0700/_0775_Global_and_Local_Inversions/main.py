from typing import List


class Solution:
    # Time Limit Exceeded
    def isIdealPermutation(self, nums: List[int]) -> bool:
        n = len(nums)
        li = sum([1 for i in range(n - 1) if nums[i] > nums[i + 1]])

        def mergeSort(left, right):
            if left >= right:
                return 0

            mi, res = (right - left) // 2 + left, 0
            res += mergeSort(left, mi)
            res += mergeSort(mi + 1, right)

            i, j, arr = left, mi + 1, list()
            while i <= mi and j <= right:
                if nums[i] < nums[j]:
                    res += j - mi - 1
                    arr.append(nums[i])
                    i += 1
                else:
                    arr.append(nums[j])
                    j += 1

            while i <= mi:
                res += j - mi - 1
                arr.append(nums[i])
                i += 1

            while j <= right:
                arr.append(nums[j])
                j += 1

            nums[left: right + 1] = arr
            return res

        gi = mergeSort(0, n - 1)
        return gi == li

    def isIdealPermutation2(self, nums: List[int]) -> bool:
        n, cMax = len(nums), 0
        for i in range(n - 2):
            cMax = max(cMax, nums[i])
            if cMax > nums[i + 2]:
                return False
        return True


if __name__ == '__main__':
    Solution().isIdealPermutation([0, 1, 2, 3])
