from python3.common.define import TreeNode


class Solution:
    # stack
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        st = list()
        while root:
            st.append(root)
            root = root.left

        while st:
            cur = st.pop()
            if k == 1:
                return cur.val
            k -= 1
            cur = cur.right
            while cur:
                st.append(cur)
                cur = cur.left

    # morris travel
    def kthSmallest2(self, root: TreeNode, k: int) -> int:
        while root:
            if not root.left:
                if k == 1:
                    return root.val
                k -= 1
                root = root.right
            else:
                cur = root.left
                while cur.right and cur.right != root:
                    cur = cur.right

                if not cur.right:
                    cur.right = root
                    root = root.left
                else:
                    cur.right = None
                    if k == 1:
                        return root.val
                    k -= 1
                    root = root.right

    # recursive
    def kthSmallest3(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.res = 0
        self.helper(root)
        return self.res

    def helper(self, root: TreeNode):
        if root:
            self.helper(root.left)
            self.k -= 1
            if not self.k:
                self.res = root.val
            self.helper(root.right)
