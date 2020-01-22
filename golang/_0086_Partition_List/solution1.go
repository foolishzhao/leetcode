package main

import "leetcode/golang/common"

type ListNode = common.ListNode

func partition(head *ListNode, x int) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	dummy1, dummy2 := new(ListNode), new(ListNode)
	tail1, tail2 := dummy1, dummy2
	for head != nil {
		if head.Val < x {
			tail1.Next = head
			tail1 = tail1.Next
		} else {
			tail2.Next = head
			tail2 = tail2.Next
		}
		head = head.Next
	}

	tail1.Next = dummy2.Next
	tail2.Next = nil
	return dummy1.Next
}
