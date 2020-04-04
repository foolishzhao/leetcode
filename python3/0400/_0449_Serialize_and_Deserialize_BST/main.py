from python3.common.define import TreeNode
import collections


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""

        res = [str(root.val)]
        if root.left:
            res.append(self.serialize(root.left))
        if root.right:
            res.append(self.serialize(root.right))

        return ",".join(res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None

        return self.deserializeHelper([int(x) for x in data.split(",")])

    def deserializeHelper(self, nums):
        if not nums:
            return None

        root = TreeNode(nums[0])
        i = 1
        while i < len(nums) and nums[i] < nums[0]:
            i += 1
        root.left = self.deserializeHelper(nums[1:i])
        root.right = self.deserializeHelper(nums[i:])
        return root


class Codec2:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""

        res, st = list(), [root]
        while st:
            cur = st.pop()
            if not cur:
                continue

            res.append(str(cur.val))
            st.append(cur.right)
            st.append(cur.left)

        return ",".join(res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None

        return self.helper(collections.deque(int(x) for x in data.split(",")), float('-inf'), float('inf'))

    def helper(self, nums, lower, upper):
        if not nums or not (lower < nums[0] < upper):
            return None

        val = nums.popleft()
        root = TreeNode(val)
        root.left = self.helper(nums, lower, val)
        root.right = self.helper(nums, val, upper)
        return root
