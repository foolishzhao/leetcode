def isBadVersion(version):
    pass


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = (right - left) // 2 + left
            if isBadVersion(mid):
                if mid == left or not isBadVersion(mid - 1):
                    return mid
                right = mid - 1
            else:
                left = mid + 1

        return 0
