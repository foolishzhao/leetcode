package main

import "leetcode/golang/common"

type TreeNode = common.TreeNode

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}

	leftRes := maxDepth(root.Left)
	rightRes := maxDepth(root.Right)

	return max(leftRes, rightRes) + 1
}

func max(x, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}
