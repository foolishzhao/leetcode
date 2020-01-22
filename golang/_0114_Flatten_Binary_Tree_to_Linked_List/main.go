package main

import "leetcode/golang/common"

type TreeNode = common.TreeNode

func flatten(root *TreeNode) {
	root = flattenHelper(root)
}

func flattenHelper(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}

	lRes := flattenHelper(root.Left)
	rRes := flattenHelper(root.Right)

	root.Left, root.Right = nil, nil
	cur := root
	cur.Right = lRes
	for cur.Right != nil {
		cur = cur.Right
	}
	cur.Right = rRes

	return root
}

// recursive
func flatten2(root *TreeNode) {
	var prev *TreeNode
	stack := []*TreeNode{root}

	for len(stack) > 0 {
		cur := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		if cur != nil {
			stack = append(stack, cur.Right)
			stack = append(stack, cur.Left)

			if prev != nil {
				prev.Right = cur
			}

			prev = cur
			prev.Left, prev.Right = nil, nil
		}
	}
}
