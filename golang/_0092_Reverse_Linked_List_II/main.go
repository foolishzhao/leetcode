package main

import "leetcode/golang/common"

type ListNode = common.ListNode

func reverseBetween(head *ListNode, m int, n int) *ListNode {
	dummy := new(ListNode)
	tail := dummy
	cur := 1
	for cur < m {
		tail.Next = head
		tail = tail.Next
		head = head.Next
		cur++
	}

	tail.Next = nil
	for cur <= n {
		next := head.Next
		head.Next = tail.Next
		tail.Next = head
		head = next
		cur++
	}

	for tail.Next != nil {
		tail = tail.Next
	}
	tail.Next = head

	return dummy.Next
}
