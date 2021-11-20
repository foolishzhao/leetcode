from typing import Optional, List

from python3.common.define import TreeNode


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        self.dfs(root, targetSum, [], res)
        return res

    def dfs(self, root, targetSum, ls, res):
        if root:
            if not root.left and not root.right and targetSum == root.val:
                ls.append(root.val)
                res.append(ls)
            self.dfs(root.right, targetSum - root.val, ls + [root.val], res)
            self.dfs(root.left, targetSum - root.val, ls + [root.val], res)


    def dfs2(self,root,targetsum,ls,res):
        if root:
            if not root.left and not root.right and targetsum ==root.val:
                ls.append(root)
                res.append(ls)
            self.dfs2(root.left,targetsum-root.left,ls+[root.val],res)
            self.dfs2(root.right,targetsum-root.right,ls+[root.val],res)
