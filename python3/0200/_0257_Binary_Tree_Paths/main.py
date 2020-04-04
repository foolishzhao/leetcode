from python3.common.define import TreeNode
from typing import List


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        self.helper(res, [], root)
        return res

    def helper(self, res, curRes, root):
        if not root:
            return

        # note: curRes += [str(root.val)] is different
        curRes = curRes + [str(root.val)]
        if not root.left and not root.right:
            res.append("->".join(curRes))
        else:
            self.helper(res, curRes, root.left)
            self.helper(res, curRes, root.right)

    # iterate
    def binaryTreePaths2(self, root: TreeNode) -> List[str]:
        res, st = [], [(root, [])]
        while st:
            node, curRes = st.pop()
            if node:
                curRes = curRes + [str(node.val)]
                if not node.left and not node.right:
                    res.append("->".join(curRes))
                else:
                    st.append((node.left, curRes))
                    st.append((node.right, curRes))

        return res


if __name__ == '__main__':
    li = [1]
    addr1 = id(li)
    li += [2]
    addr2 = id(li)
    assert addr1 == addr2

    li = li + [3]
    addr3 = id(li)
    assert addr1 != addr3

    print(addr1)
    print(addr2)
    print(addr3)
