from python3.common.define import TreeNode


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""
        return self.dfs(t)

    def dfs(self, t):
        if not t.left and not t.right:
            return str(t.val)
        if not t.left:
            return str(t.val) + '()' + '(' + self.dfs(t.right) + ')'
        if not t.right:
            return str(t.val) + '(' + self.dfs(t.left) + ')'
        return str(t.val) + '(' + self.dfs(t.left) + ')(' + self.dfs(t.right) + ')'
