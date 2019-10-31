package main

import "leetcode/golang/common"

type ListNode = common.ListNode

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	if l1 == nil {
		return l2
	} else if l2 == nil {
		return l1
	} else {
		dummy := &ListNode{}
		cur := dummy
		carry := 0

		for ; l1 != nil || l2 != nil || carry > 0; {
			t := carry

			if l1 != nil {
				t += l1.Val
				l1 = l1.Next
			}

			if l2 != nil {
				t += l2.Val
				l2 = l2.Next
			}

			carry = t / 10

			cur.Next = &ListNode{Val: t % 10}
			cur = cur.Next
		}

		return dummy.Next
	}
}
