class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def removeNthFromEnd(self, head,n):
        if head.next==None:
            return None
        tmp = head
        size = 0
        while tmp:
            size += 1
            tmp = tmp.next
        tmp = head
        if n == size:
            return head.next

        for i in range(size - n - 1):
            tmp = tmp.next
        tmp.next = tmp.next.next
        return head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    Solution().removeNthFromEnd([1,2,3,4,5], 2)