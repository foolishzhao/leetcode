package main

import "leetcode/golang/common"

type TreeNode = common.TreeNode

func minDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}

	if root.Left == nil && root.Right == nil {
		return 1
	} else if root.Left == nil {
		return minDepth(root.Right) + 1
	} else if root.Right == nil {
		return minDepth(root.Left) + 1
	} else {
		lDepth := minDepth(root.Left)
		rDepth := minDepth(root.Right)

		return min(lDepth, rDepth) + 1
	}
}

func min(x, y int) int {
	if x < y {
		return x
	} else {
		return y
	}
}
