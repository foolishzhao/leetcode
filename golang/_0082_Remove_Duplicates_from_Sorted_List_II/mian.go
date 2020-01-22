package main

import "leetcode/golang/common"

type ListNode = common.ListNode

func deleteDuplicates(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	dummy := new(ListNode)
	tail := dummy
	for head != nil {
		if head.Next == nil || head.Next.Val != head.Val {
			tail.Next = head
			tail = tail.Next
		} else {
			for head.Next != nil && head.Next.Val == head.Val {
				head = head.Next
			}
		}

		head = head.Next
	}

	tail.Next = nil

	return dummy.Next
}
