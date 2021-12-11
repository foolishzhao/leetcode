from python3.common.define import ListNode
class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        import heapq
        dummy = ListNode(0)
        tail = dummy
        pq = []
        for i in range(len(lists)):
            if lists[i] :
                heapq.heappush(pq, (lists[i].val, i))
                lists[i] = lists[i].next
        while pq:
            val, idx = heapq.heappop(pq)
            tail.next = ListNode(val)
            tail = tail.next
            lists[idx] = lists[idx].next
            if lists[idx]:
                heapq.heappush(pq, (lists[idx].val, idx))

        return dummy.next
