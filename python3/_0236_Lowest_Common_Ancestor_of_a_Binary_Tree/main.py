from python3.common.define import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        elif root == p or root == q:
            return root
        else:
            lRes = self.lowestCommonAncestor(root.left, p, q)
            rRes = self.lowestCommonAncestor(root.right, p, q)
            if lRes and rRes:
                return root
            elif lRes:
                return lRes
            else:
                return rRes

    #
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        dt = {root: None}
        queue = [root]
        while p not in dt or q not in dt:
            cur = queue.pop(0)

            if cur.left:
                dt[cur.left] = cur
                queue.append(cur.left)

            if cur.right:
                dt[cur.right] = cur
                queue.append(cur.right)

        ancestors = set()
        while p:
            ancestors.add(p)
            p = dt[p]

        while q and q not in ancestors:
            q = dt[q]

        return q
