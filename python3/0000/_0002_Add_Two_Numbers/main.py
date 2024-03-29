from python3.common.define import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = tail = ListNode(0)
        c = 0
        while l1 or l2 or c:
            if l1:
                c += l1.val
                l1 = l1.next

            if l2:
                c += l2.val
                l2 = l2.next

            tail.next = ListNode(c % 10)
            tail = tail.next

            c //= 10

        return dummy.next

if __name__ == '__main__':
    arr1 = [ListNode(x) for x in list(range(1, 6))]
    for i, node in enumerate(arr1[:-1]):
        node.next = arr1[i + 1]
    arr2 = [ListNode(x) for x in list(range(5, 9))]
    for i, node in enumerate(arr2[:-1]):
        node.next = arr2[i + 1]


    Solution().addTwoNumbers(arr1[0],arr2[0])
