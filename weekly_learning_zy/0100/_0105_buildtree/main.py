import collections
from typing import Optional, List
from python3.common.define import TreeNode
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder,inorder[0:ind])
            root.right = self.buildTree(preorder,inorder[ind+1:])
            return root
