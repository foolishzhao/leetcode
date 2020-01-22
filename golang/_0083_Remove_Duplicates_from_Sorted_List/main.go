package main

import "leetcode/golang/common"

type ListNode = common.ListNode

func deleteDuplicates(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	prev, cur := head, head.Next
	for cur != nil {
		if cur.Val != prev.Val {
			prev.Next = cur
			prev = prev.Next
		}

		cur = cur.Next
	}
	prev.Next = nil

	return head
}
