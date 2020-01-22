package main

import "leetcode/golang/common"

type TreeNode = common.TreeNode

func pathSum(root *TreeNode, sum int) [][]int {
	res := make([][]int, 0)
	pathSumHelper(root, sum, &res, []int{})

	return res
}

func pathSumHelper(root *TreeNode, sum int, res *[][]int, oneRes []int) {
	if root == nil {
		return
	}

	if root.Left == nil && root.Right == nil && root.Val == sum {
		*res = append(*res, append([]int{}, append(oneRes, root.Val)...))
		return
	}

	pathSumHelper(root.Left, sum-root.Val, res, append(oneRes, root.Val))
	pathSumHelper(root.Right, sum-root.Val, res, append(oneRes, root.Val))
}
