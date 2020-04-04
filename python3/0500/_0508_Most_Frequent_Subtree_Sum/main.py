import collections
from python3.common.define import TreeNode
from typing import List


class Solution:
    def __init__(self):
        self.dt = collections.defaultdict(int)

    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return list()

        self.treeSum(root)
        maxFreq = max(self.dt.values())
        return [k for k, v in self.dt.items() if v == maxFreq]

    def treeSum(self, root):
        if not root:
            return 0

        s = self.treeSum(root.left) + root.val + self.treeSum(root.right)
        self.dt[s] += 1
        return s
