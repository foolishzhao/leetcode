# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        arr = self.inorderTraversal(root)
        ans = []
        for i in range(len(arr) - 1):
            ans.append(arr[i + 1] - arr[i])

        return min(ans)

        pre = -float('inf')
        res = float('inf')

        def minDiffInBST(self, root):
            if root is None:
                return

            self.minDiffInBST(root.left)
            # evaluate and set the current node as the node previously evaluated
            self.res = min(self.res, root.val - self.pre)
            self.pre = root.val

            self.minDiffInBST(root.right)
            return self.res
