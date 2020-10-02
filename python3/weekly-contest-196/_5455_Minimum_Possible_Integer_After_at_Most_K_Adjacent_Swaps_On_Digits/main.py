class BIT:
    def __init__(self, n):
        self.nums = [0] * (n + 1)
        self.n = n

    def update(self, i, delta):
        i += 1
        while i <= self.n:
            self.nums[i] += delta
            i += i & -i

    def prefixSum(self, i):
        res, i = 0, i + 1
        while i:
            res += self.nums[i]
            i -= i & -i
        return res


class Solution:
    def minInteger(self, num: str, k: int) -> str:
        num, n = list(num), len(num)
        if k >= n * (n - 1) // 2:
            num.sort()
        else:
            i = 0
            while i < n and k:
                mIdx = i
                for j in range(i + 1, min(i + k + 1, n)):
                    if num[j] < num[mIdx]:
                        mIdx = j
                num[i: mIdx + 1] = [num[mIdx]] + num[i: mIdx]
                k -= mIdx - i
                i += 1

        return ''.join(num)

    def minInteger2(self, num: str, k: int) -> str:
        if not k:
            return num

        n = len(num)
        if k >= n * (n - 1) // 2:
            return "".join(sorted(list(num)))

        # for each number, find the first index
        for i in range(10):
            ind = num.find(str(i))
            if 0 <= ind <= k:
                return str(num[ind]) + self.minInteger(num[0:ind] + num[ind + 1:], k - ind)

    # O(n*log(n))
    def minInteger3(self, num: str, k: int) -> str:
        num, n = list(num), len(num)
        if k >= n * (n - 1) // 2:
            return ''.join(sorted(num))
        else:
            idxList = [list() for _ in range(10)]
            for i, d in enumerate(num):
                idxList[int(d)].append(i)

            res, bit = "", BIT(n)
            for i in range(n):
                for j in range(10):
                    if not idxList[j]:
                        continue

                    # bit stores idx which shifted to front before
                    # idx - shift is how many steps need to mov idx to current front
                    idx = idxList[j][0]
                    shift = bit.prefixSum(idx)
                    if idx - shift <= k:
                        idxList[j].pop(0)
                        k -= idx - shift
                        bit.update(idx, 1)
                        res += str(j)
                        break

            return res
