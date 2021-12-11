"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # 广度优先搜索，借助队列完成--需要先进先出，只要队列不为空 ，就打印当前节点并且弹出，
        if not root:
            return None
        res = []
        # list 这个结构弹出首元素的时间复杂度是O(n)
        # deque 底层结构是链表，弹出首元素的时间复杂度是O(1)
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                queue.append(node.right)
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
        return root

