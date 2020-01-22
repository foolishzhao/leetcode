package main

import "leetcode/golang/common"

type TreeNode = common.TreeNode

// recursive
func inorderTraversal(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}

	leftRes := inorderTraversal(root.Left)
	rightRes := inorderTraversal(root.Right)

	return append(append(leftRes, root.Val), rightRes...)
}

// iterate, O(n) time, O(h) space
func inorderTraversal2(root *TreeNode) []int {
	res := make([]int, 0)

	stack := make([]*TreeNode, 0)
	for root != nil {
		stack = append(stack, root)
		root = root.Left
	}

	for len(stack) > 0 {
		cur := stack[len(stack)-1]
		stack = stack[0 : len(stack)-1]

		res = append(res, cur.Val)

		cur = cur.Right
		for cur != nil {
			stack = append(stack, cur)
			cur = cur.Left
		}
	}

	return res
}

// iterate, O(n) time, O(1) space
func inorderTraversal3(root *TreeNode) []int {
	res := make([]int, 0)

	for root != nil {
		if root.Left == nil {
			res = append(res, root.Val)
			root = root.Right
		} else {
			cur := root.Left
			for cur.Right != nil && cur.Right != root {
				cur = cur.Right
			}

			if cur.Right == nil {
				cur.Right = root
				root = root.Left
			} else {
				cur.Right = nil
				res = append(res, root.Val)
				root = root.Right
			}
		}
	}

	return res
}

func main() {
	root := &TreeNode{
		Val: 1,
		Right: &TreeNode{
			Val: 2,
			Left: &TreeNode{
				Val: 3,
			},
		},
	}

	inorderTraversal2(root)
}
