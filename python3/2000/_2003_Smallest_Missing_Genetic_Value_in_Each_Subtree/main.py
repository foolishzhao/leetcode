import collections
from typing import List


class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        res = [1] * len(parents)
        if 1 not in nums:
            return res

        children = collections.defaultdict(list)
        for c, p in enumerate(parents):
            children[p].append(c)

        def dfs(i):
            if not seen[nums[i]]:
                for c in children[i]:
                    dfs(c)
                seen[nums[i]] = True

        seen = [False] * 100005
        cur, miss = nums.index(1), 1
        while cur != -1:
            dfs(cur)
            while seen[miss]:
                miss += 1
            res[cur] = miss
            cur = parents[cur]

        return res
