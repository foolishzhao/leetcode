class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None
