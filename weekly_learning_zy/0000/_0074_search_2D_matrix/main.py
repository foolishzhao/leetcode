from _ast import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n - 1
        while low <= high:
            mid = (low + high) // 2
            i, j = mid // n, mid % n
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height = len(matrix)
        r = len(matrix[0]) - 1

        l, p = 0, 0

        while p < height:
            if matrix[p][l] <= target <= matrix[p][r]:
                while l <= r:
                    mid = (l + r) // 2
                    if matrix[p][mid] == target:
                        return True
                    elif matrix[p][mid] > target:
                        r = mid - 1
                    else:
                        l = mid + 1
            else:
                p += 1
        return False


