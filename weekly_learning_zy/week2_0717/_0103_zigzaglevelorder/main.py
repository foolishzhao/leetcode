# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, root, level, res):
        if root:
            if len(res) == level:
                res.append([])
            if level % 2 == 0:
                res[level].append(root.val)
                self.dfs(root.left, level + 1, res)
                self.dfs(root.right, level + 1, res)
            else:
                res[level].insert(0, root.val)
                self.dfs(root.left, level + 1, res)
                self.dfs(root.right, level + 1, res)
