from python3.common.define import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = tail = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = carry + x + y
            carry = s // 10
            tail.next = ListNode(s % 10)
            tail = tail.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


if __name__ == '__main__':
    arr1 = [ListNode(x) for x in list(range(1, 6))]
    for i, node in enumerate(arr1[:-1]):
        node.next = arr1[i + 1]
    arr2 = [ListNode(x) for x in list(range(5, 9))]
    for i, node in enumerate(arr2[:-1]):
        node.next = arr2[i + 1]

    l3 = Solution().addTwoNumbers(arr1[0], arr2[0])
    while l3:
        print(l3.val)
        l3 = l3.next
