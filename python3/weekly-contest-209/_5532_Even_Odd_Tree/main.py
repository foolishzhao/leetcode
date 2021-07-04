from python3.common.define import TreeNode


class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        lv, q = 0, [root]
        while q:
            sz = len(q)
            prev = float('-inf') if lv % 2 == 0 else float('inf')
            for _ in range(sz):
                cur = q.pop(0)
                if not cur:
                    continue

                if lv % 2 == 0:
                    if cur.val % 2 != 1 or cur.val <= prev:
                        return False

                if lv % 2 == 1:
                    if cur.val % 2 != 0 or cur.val >= prev:
                        return False

                prev = cur.val
                q.append(cur.left)
                q.append(cur.right)
            lv += 1

        return True
