package main

import "leetcode/golang/common"

type ListNode = common.ListNode

// iterate
func reverseList(head *ListNode) *ListNode {
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

// recursive
func reverseList2(head *ListNode) *ListNode {
	head, _ = reverseListHelper(head)
	return head
}

func reverseListHelper(head *ListNode) (*ListNode, *ListNode) {
	if head == nil || head.Next == nil {
		return head, head
	}

	subHead, subTail := reverseListHelper(head.Next)
	head.Next = nil
	subTail.Next = head

	return subHead, head
}

// recursive
func reverseList3(head *ListNode) *ListNode {
	return reverseListHelper3(head, nil)
}

func reverseListHelper3(oldHead, newHead *ListNode) *ListNode {
	if oldHead == nil {
		return newHead
	}

	next := oldHead.Next
	oldHead.Next = newHead

	return reverseListHelper3(next, oldHead)
}
