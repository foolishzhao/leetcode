from python3.common.define import TreeNode
from typing import List
import collections


class Solution:
    def canMerge(self, trees: List[TreeNode]) -> TreeNode:
        dt, ind = collections.defaultdict(TreeNode), set()

        for tree in trees:
            if tree.left:
                if tree.left.val in ind:
                    return None
                ind.add(tree.left.val)
                dt[tree.left.val] = tree.left
            if tree.right:
                if tree.right.val in ind:
                    return None
                ind.add(tree.right.val)
                dt[tree.right.val] = tree.right

        for tree in trees:
            dt[tree.val] = tree

        root = [tree for tree in trees if tree.val not in ind]
        if len(root) != 1:
            return None

        def inOrder(node):
            seen.add(node)

            if node.left:
                node.left, valid = inOrder(dt[node.left.val])
                if not valid:
                    return None, False

            nonlocal prev
            if prev and prev >= node.val:
                return None, False
            prev = node.val

            if node.right:
                node.right, valid = inOrder(dt[node.right.val])
                if not valid:
                    return None, False

            return node, True

        prev, seen = None, set()
        res, valid = inOrder(root[0])
        return res if valid and len(seen) == len(dt) else None
