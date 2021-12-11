from python3.common.define import ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        dummy = tail = ListNode(0)
        while head:
            if head.next:
                t = head.next.next

                tail.next = head.next
                tail = tail.next
                tail.next = head
                tail = tail.next

                head = t
            else:
                tail.next = head
                tail = tail.next
                head = None

        tail.next = None
        return dummy.next

    def swapPairs2(self,head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = tail = ListNode(0)
        while head:
            if head.next:
                tail.next = head.next
                t = head.next.next
                tail = tail.next
                tail.next = head
                tail = tail.next
                head =t
            else:
                tail.next = head
                tail = tail.next
                head = None
        tail.next = None
        return dummy.next

if __name__ == '__main__':
    arr1 = [ListNode(x) for x in list(range(1, 8))]
    for i, node in enumerate(arr1[:-1]):
        node.next = arr1[i + 1]
    arr2 = [ListNode(x) for x in list(range(5, 9))]
    for i, node in enumerate(arr2[:-1]):
        node.next = arr2[i + 1]

    l3 = Solution().swapPairs(arr1[0])
    while l3:
        print(l3.val)
        l3 = l3.next
