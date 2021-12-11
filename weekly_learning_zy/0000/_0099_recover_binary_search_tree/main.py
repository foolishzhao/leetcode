from typing import Optional

from python3.common.define import TreeNode
#Since we get two elements that are swapped by mistake, there must be a smaller TreeNode get a larger value and a larger TreeNode get a smaller value.
#Their value are swapped, but the incorrect smaller node is still in smaller tree and incorrect larger node is still in larger tree. So we will visit the incorrect smaller node first, and this node will be detected when we compare its value with next.val, i.e. when it is treated as prev node. The incorrect larger node will be detected when we compare its value with prev.val. We don't know if it is close or not close to incorrect smaller node, so we should continue search BST and update it if we found another incorrect node.

#Therefore if it is the first time we found an incorrect pair, the prev node must be the first incorrect node.
#If it is not the first time we found an incorrect pair, the curr node must be the second incorrect node, though
#we may have corner case that two incorrect nodes are in same pair.
#这个题目的前提是我们已知在这个二叉搜索树里面，只有两个节点是被错误的交换了
#所以目的就是找到这两个节点并把他们交换过来；按照上面的分析，第一个对里 prev node 是invalid node, 第二对里cur node 是 invalid node
#按照中序遍历的算法 ,当cur<prev 的时候 记录此时的prev,cur ,循环最后给元组里的 prev,cur对做交换
class Solution:

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """s
        Do not return anything, modify root in-place instead.
        """
        stack = [(root, False)]
        prev, drops = TreeNode(float('-inf')), []
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    # add to result if visited
                    if node.val < prev.val:
                        drops.append((prev, node))
                    prev = node

                else:
                    # in-order
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        drops[0][0].val, drops[-1][1].val = drops[-1][1].val, drops[0][0].val
