package main

import "leetcode/golang/common"

type ListNode = common.ListNode

func rotateRight(head *ListNode, k int) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	k %= linkedListLen(head)
	if k == 0 {
		return head
	}

	p, q := head, head
	for i := 0; i < k; i++ {
		q = q.Next
	}

	for q.Next != nil {
		p = p.Next
		q = q.Next
	}

	newHead := p.Next
	p.Next = nil
	q.Next = head

	return newHead
}

func linkedListLen(head *ListNode) int {
	res := 0;
	for head != nil {
		res++
		head = head.Next
	}

	return res
}
