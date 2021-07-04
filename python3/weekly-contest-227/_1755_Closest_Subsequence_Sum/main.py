from typing import List
import bisect


class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        def dfs(i, cur, arr, st):
            if i == len(arr):
                st.add(cur)
                return
            dfs(i + 1, cur, arr, st)
            dfs(i + 1, cur + arr[i], arr, st)

        n, st1, st2 = len(nums) // 2, set(), set()
        dfs(0, 0, nums[:n], st1)
        dfs(0, 0, nums[n:], st2)

        li2, res = sorted(st2), abs(goal)
        for x in st1:
            j = bisect.bisect_left(li2, goal - x)
            if j < len(li2):
                res = min(res, abs(x + li2[j] - goal))
            if j:
                res = min(res, abs(x + li2[j - 1] - goal))
        return res
