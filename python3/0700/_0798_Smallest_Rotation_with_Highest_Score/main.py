class Solution:
    def bestRotation(self, nums):
        n, cnt = len(nums), [0] * len(nums)
        for i, num in enumerate(nums):
            if num > i:
                if num == n:
                    continue

                left, right = i + 1, n - num + i
                cnt[left] += 1
                if right + 1 < n:
                    cnt[right + 1] -= 1
            else:
                left, right = 0, i - num
                cnt[left] += 1
                if right + 1 < n:
                    cnt[right + 1] -= 1

                left, right = i + 1, n - num + i
                if left < n:
                    cnt[left] += 1

        for i in range(1, n):
            cnt[i] += cnt[i - 1]
        return cnt.index(max(cnt))
