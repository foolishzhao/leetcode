from typing import Optional
from python3.common.define import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        #为什么需要这一行呢？是因为当当前节点没有左/右子树的时候 ，if p and q 这一条语句就走不通了
        # (p is q) checks if p and q reference to the same object. In this case, if both p and q reference to None, then it is the same object so will return True, else False.
        # It handles the part where p or q isn't exist so isn't handled by the first condition.
        return p is q