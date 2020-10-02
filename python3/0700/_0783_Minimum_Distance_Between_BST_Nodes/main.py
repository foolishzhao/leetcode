from python3.common.define import TreeNode


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        res, prev = float('inf'), float('-inf')
        st = list()
        while root or st:
            while root:
                st.append(root)
                root = root.left

            root = st.pop()
            res = min(res, root.val - prev)
            prev = root.val
            root = root.right

        return res
