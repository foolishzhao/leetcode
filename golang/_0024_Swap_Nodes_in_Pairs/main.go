package main

import "leetcode/golang/common"

type ListNode = common.ListNode

func swapPairs(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	dummy := new(ListNode)
	tail, pre := dummy, head
	for pre != nil {
		p := pre.Next
		if p == nil {
			tail.Next = pre
			tail = tail.Next
			break
		}

		next := p.Next

		tail.Next = p
		tail = tail.Next
		tail.Next = pre
		tail = tail.Next

		pre = next
	}

	tail.Next = nil
	return dummy.Next
}
