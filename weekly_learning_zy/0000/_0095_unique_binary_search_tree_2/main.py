from python3.common.define import TreeNode
from typing import List, Optional


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        return self.helper(1, n)

    def helper(self, start, end):
        if start > end:  # edge case, see exposition below
            return [None]

        all_trees = []  # list of all unique BSTs
        for curRootVal in range(start, end + 1):
            all_left_subtrees = self.helper(start, curRootVal - 1)
            all_right_subtrees = self.helper(curRootVal + 1, end)

            for left_subtree in all_left_subtrees:
                for right_subtree in all_right_subtrees:
                    curRoot = TreeNode(curRootVal)
                    curRoot.left = left_subtree
                    curRoot.right = right_subtree

                    # curRoot is now the root of a BST
                    all_trees.append(curRoot)

        return all_trees

if __name__ == '__main__':
    print(Solution().generateTrees(5))