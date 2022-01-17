from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not len(matrix) or not len(matrix[0]):
            # Quick response for empty matrix
            return False

        h, w = len(matrix), len(matrix[0])

        for row in matrix:

            # range check
            if row[0] <= target <= row[-1]:

                # launch binary search on current possible row

                left, right = 0, w - 1

                while left <= right:

                    mid = left + (right - left) // 2

                    mid_value = row[mid]

                    if target > mid_value:
                        left = mid + 1
                    elif target < mid_value:
                        right = mid - 1
                    else:
                        return True

        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height = len(matrix)
        r = len(matrix[0]) - 1

        l, p = 0, 0

        for p in range(height):
            l, r = 0, len(matrix[0]) - 1
            if matrix[p][l] <= target <= matrix[p][r]:
                while l <= r:
                    mid = (l + r) // 2
                    if matrix[p][mid] == target:
                        return True
                    elif matrix[p][mid] > target:
                        r = mid - 1
                    else:
                        l = mid + 1

        return False