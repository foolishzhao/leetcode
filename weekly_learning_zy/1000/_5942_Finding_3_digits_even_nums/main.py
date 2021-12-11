from typing import List


class Solution:
    def atn(self, a):
        a = [i * 10 ** index for index, i in enumerate(a[::-1])]
        b = sum(a)
        return b
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        def dfs(nums, curRes):
            ans = self.atn(curRes)
            if len(curRes)==3 and ans % 2 == 0 and curRes[0] != 0:
                if ans not in res:
                    res.append(ans)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                dfs(nums[:i] + nums[i+1:], curRes + [nums[i]])
        res = []
        dfs(sorted(digits), [])
        return sorted(res)

    def findEvenNumbers2(self, digits: List[int]) -> List[int]:
        # for every index as digit and value is count
        d = [0] * 10
        for x in digits:
            d[x] = d[x] + 1

        ans = []

        # loop through all possible numbers
        for number in range(100, 999, 2):
            # find three digit to build this number
            d1 = number // 100
            d2 = (number - d1 * 100) // 10
            d3 = number - d1 * 100 - d2 * 10

            # check if we get enough digits
            check = d.copy()
            print(check)
            check[d1] -= 1
            check[d2] -= 1
            check[d3] -= 1

            if check[d1] >= 0 and check[d2] >= 0 and check[d3] >= 0:
                ans.append(number)

        return ans


if __name__ == '__main__':
    a = [1,8,7,7,1,1,5,4,0,0,7,5,1,7,9]

    r = Solution().findEvenNumbers2(a)
    print(r)

