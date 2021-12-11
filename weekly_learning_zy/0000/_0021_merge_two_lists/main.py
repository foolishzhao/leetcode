wfrom python3.common.define import ListNode
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(None)
        node = res
        while l1 and l2:
            if l1.val<l2.val:
                node.next,l1 = l1,l1.next
            else:
                node.next,l2 = l2,l2.next
            node = node.next
        if l1:
            node.next = l1
        else:
            node.next = l2
        return res.next
    def mergeTwoLists2(self,l1: ListNode,l2: ListNode) -> ListNode:

        dummy = tail = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        else:
            tail.next = l2
        return dummy.next

if __name__ == '__main__':
    arr1 = [ListNode(x) for x in list(range(1, 6))]
    for i, node in enumerate(arr1[:-1]):
        node.next = arr1[i + 1]
    arr2 = [ListNode(x) for x in list(range(5, 9))]
    for i, node in enumerate(arr2[:-1]):

        node.next = arr2[i + 1]
    l3 = Solution().mergeTwoLists(arr1[0], arr2[0])
    while l3:
        print(l3.val)
        l3 = l3.next