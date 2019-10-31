package main

import "leetcode/golang/common"

type ListNode = common.ListNode

func reverseKGroup(head *ListNode, k int) *ListNode {
	if head == nil || head.Next == nil || k <= 1 {
		return head
	}

	dummy := new(ListNode)
	tail := dummy
	for head != nil {
		pre := head
		i := 0
		for i < k-1 && pre.Next != nil {
			i++
			pre = pre.Next
		}

		if i < k-1 {
			tail.Next = head
			break
		}

		nextHead := pre.Next
		pre.Next = nil
		tail.Next = reverse(head)
		for tail.Next != nil {
			tail = tail.Next
		}

		head = nextHead
	}

	return dummy.Next
}

func reverse(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	dummy := new(ListNode)
	for head != nil {
		next := head.Next
		head.Next = dummy.Next
		dummy.Next = head
		head = next
	}

	return dummy.Next
}
