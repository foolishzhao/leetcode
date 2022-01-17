class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        def find(i, j):
            # if cannot find, return the less one
            # when the recursion is end.
            if j < i:
                return j
            m = (i + j) // 2
            m_ = m * m
            # if find
            if m_ == x:
                return m
            elif m_ < x:
                return find(m + 1, j)
            else:
                return find(i, m - 1)

        return find(0, x)