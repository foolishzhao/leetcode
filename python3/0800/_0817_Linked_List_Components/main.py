from python3.common.define import ListNode
from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[px] = py


class Solution:
    def numComponents(self, head: ListNode, nums: List[int]) -> int:
        nums, prev = set(nums), None

        n, p = 0, head
        while p:
            n += 1
            p = p.next

        uf = UnionFind(n)
        while head:
            if prev is not None and prev in nums and head.val in nums:
                uf.union(prev, head.val)

            prev = head.val
            head = head.next

        comp = set()
        for num in nums:
            comp.add(uf.find(num))
        return len(comp)

    def numComponents2(self, head: ListNode, nums: List[int]) -> int:
        res, nums = 0, set(nums)
        prev = False
        while head:
            if head.val in nums:
                if not prev:
                    res += 1
                prev = True
            else:
                prev = False
            head = head.next
        return res
