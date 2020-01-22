package main

import "leetcode/golang/common"

type TreeNode = common.TreeNode

func isBalanced(root *TreeNode) bool {
	_, valid := isBalancedHelper(root)
	return valid
}

func isBalancedHelper(root *TreeNode) (int, bool) {
	if root == nil {
		return 0, true
	}

	lDepth, lValid := isBalancedHelper(root.Left)
	rDepth, rValid := isBalancedHelper(root.Right)

	return max(lDepth, rDepth) + 1, lValid && rValid && rDepth-1 <= lDepth && lDepth <= rDepth+1
}

func max(x, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}
