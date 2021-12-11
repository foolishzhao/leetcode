import collections
from typing import Optional, List

from python3.common.define import TreeNode

class Solution:
#func1 BFS
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 广度优先搜索，借助队列完成--需要先进先出，只要队列不为空 ，就打印当前节点并且弹出，
        if not root:
            return []
        res = []
        # list 这个结构弹出首元素的时间复杂度是O(n)
        # deque 底层结构是链表，弹出首元素的时间复杂度是O(1)
        queue = collections.deque()
        queue.append(root)
        while queue:
            cur_level, size = [], len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur_level.append(node.val)
            res.append(cur_level)
        return res
# func2 Recursively dfs
    def levelOrder(self, root):
        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, root, level, res):
        if root:
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            self.dfs(root.left, level + 1, res)
            self.dfs(root.right, level + 1, res)
