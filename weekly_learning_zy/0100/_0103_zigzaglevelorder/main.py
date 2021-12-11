# Definition for a binary tree node.
import collections


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
    #BFS
    def zigzagLevelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        # list 这个结构弹出首元素的时间复杂度是O(n)
        # deque 底层结构是链表，弹出首元素的时间复杂度是O(1)
        queue = collections.deque()
        queue.append(root)
        level = 1
        while queue:
            cur_level, size = [], len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur_level.append(node.val)
            if level % 2 == 0:
                res.append(cur_level[::-1])
            else:
                res.append(cur_level)
            level += 1
        return res