from python3.common.define import TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        queue = [root]
        while queue:
            cur = queue.pop(0)
            if cur:
                res.append(str(cur.val))
                queue.append(cur.left)
                queue.append(cur.right)
            else:
                res.append("null")

        return " ".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        nodes = [TreeNode(int(x)) if x != 'null' else None for x in data.split()]

        root = nodes[0]
        queue = [root]
        i = 1
        while queue:
            cur = queue.pop(0)
            if cur:
                cur.left = nodes[i]
                cur.right = nodes[i + 1]
                i += 2

                queue.append(cur.left)
                queue.append(cur.right)

        return root
