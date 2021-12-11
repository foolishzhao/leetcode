import collections
from typing import List

from python3.common.define import TreeNode


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node):
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                dfs(node.left)

            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                dfs(node.right)

        graph = collections.defaultdict(list)
        dfs(root)

        q, seen = [target], {target}
        while q and k > 0:
            sz = len(q)
            k -= 1
            for _ in range(sz):
                u = q.pop(0)
                for v in graph[u]:
                    if v not in seen:
                        q.append(v)
                        seen.add(v)
        return q

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    print(Solution().distanceK(
        root,
        5,
        2,
    ))