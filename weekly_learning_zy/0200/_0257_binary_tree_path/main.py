from typing import Optional

from python3.common.define import TreeNode


class Solution:
    def binaryTreePaths(self, root: sTreeNode) -> List[str]:
        res = []
        self.helper(res, [], root)
        return res

    def helper(self, res, curRes, root):
        if not root:
            return

        # note: curRes += [str(root.val)] is different
        curRes = curRes + [str(root.val)]
        if not root.left and not root.right:
            res.append("->".join(curRes))
        else:
            self.helper(res, curRes, root.left)
            self.helper(res, curRes, root.right)

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(curRes, curNode):
            if not curNode:
                return

            curRes.append(str(curNode.val))
            if not curNode.left and not curNode.right:
                res.append('->'.join(curRes))
            else:
                dfs(curRes, curNode.left)
                dfs(curRes, curNode.right)
            curRes.pop()

        res = list()
        dfs(list(), root)
        return res
    def binaryTreePaths(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        treepaths = [str(root.val) + '->' + path for path in self.binaryTreePaths(root.left)]
        treepaths += [str(root.val) + '->' + path for path in self.binaryTreePaths(root.right)]
        return treepaths