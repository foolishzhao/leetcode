from python3.common.define import TreeNode


class Solution:
    # recursive
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        prevLeft = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(prevLeft)

        return root

    # iterate
    def invertTree2(self, root: TreeNode) -> TreeNode:
        st = [root]
        while st:
            cur = st.pop()
            if not cur:
                continue

            prevLeft = cur.left
            cur.left = cur.right
            cur.right = prevLeft

            st.append(cur.left)
            st.append(cur.right)

        return root
