package main

import "leetcode/golang/common"

type ListNode = common.ListNode
type TreeNode = common.TreeNode

func sortedListToBST(head *ListNode) *TreeNode {
	if head == nil {
		return nil
	}

	dummy := &ListNode{
		Next: head,
	}
	slow, fast := dummy, dummy
	for fast.Next != nil && fast.Next.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	root := &TreeNode{
		Val:   slow.Next.Val,
		Right: sortedListToBST(slow.Next.Next),
	}

	slow.Next = nil
	root.Left = sortedListToBST(dummy.Next)

	return root
}
