package main

import "leetcode/golang/common"

type ListNode = common.ListNode

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	if head == nil && n <= 0 {
		return nil
	}

	dummy := new(ListNode)
	dummy.Next = head

	pre, p := dummy, head

	for n > 0 {
		p = p.Next
		n--
	}

	for p != nil {
		pre = pre.Next
		p = p.Next
	}
	pre.Next = pre.Next.Next

	return dummy.Next
}
