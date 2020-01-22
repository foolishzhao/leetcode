package main

import (
	"leetcode/golang/common"
	"math"
)

type TreeNode = common.TreeNode

// recursive
func isValidBST(root *TreeNode) bool {
	_, _, res := dfs(root)
	return res
}

func dfs(root *TreeNode) (int, int, bool) {
	if root == nil {
		return math.MaxInt64, math.MinInt64, true
	} else {
		rootVal := root.Val
		lMin, lMax, lValid := dfs(root.Left)
		rMin, rMax, rValid := dfs(root.Right)
		valid := lValid && rValid && lMax < rootVal && rootVal < rMin
		return min(rootVal, lMin), max(rootVal, rMax), valid
	}
}

func max(x, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}

func min(x, y int) int {
	if x < y {
		return x
	} else {
		return y
	}
}

// recursive
func isValidBST2(root *TreeNode) bool {
	return isValidBSTHelper(root, math.MinInt64, math.MaxInt64)
}

func isValidBSTHelper(root *TreeNode, curMin, curMax int) bool {
	if root == nil {
		return true
	}
	curVal := root.Val
	return curVal > curMin &&
		curVal < curMax &&
		isValidBSTHelper(root.Left, curMin, curVal) &&
		isValidBSTHelper(root.Right, curVal, curMax)
}

// morris
func isValidBST3(root *TreeNode) bool {
	prev := math.MinInt64
	for root != nil {
		if root.Left == nil {
			if prev >= root.Val {
				return false
			}
			prev = root.Val
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
				if prev >= root.Val {
					return false
				}
				prev = root.Val
				root = root.Right
			}
		}
	}

	return true
}

func main() {
	root := &TreeNode{
		Val: 5,
		Left: &TreeNode{
			Val: 14,
			Left: &TreeNode{
				Val: 1,
			},
		},
	}

	isValidBST(root)
}
