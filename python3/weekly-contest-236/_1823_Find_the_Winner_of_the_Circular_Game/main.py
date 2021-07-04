class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def game(li, idx):
            if len(li) == 1:
                return li[0]

            curK, curN = k, len(li)
            while curK > 1:
                idx = (idx + 1) % curN
                curK -= 1

            return game(li[:idx] + li[idx + 1:], idx % (curN - 1))

        return game(list(range(1, n + 1)), 0)

    def findTheWinner2(self, n: int, k: int) -> int:
        nums = list(range(1, n + 1))

        i, k = k - 1, k - 1
        while len(nums) > 1:
            nums.pop(i)
            i = (i + k) % len(nums)
        return nums[0]
