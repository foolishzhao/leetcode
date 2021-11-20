from typing import Optional, List
from python3.common.define import TreeNode
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        ind = inorder.index(postorder.pop())
        root = TreeNode(inorder[ind])
        root.left = self.buildTree(inorder[0:ind], postorder[:ind])
        root.right = self.buildTree(inorder[ind + 1:], postorder[ind:])

        return root
