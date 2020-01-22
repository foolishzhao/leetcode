package main

import "leetcode/golang/common"

type TreeNode = common.TreeNode

func sortedArrayToBST(nums []int) *TreeNode {
	return sortedArrayToBSTHelper(nums, 0, len(nums)-1)
}

func sortedArrayToBSTHelper(nums []int, begin, end int) *TreeNode {
	if begin > end {
		return nil
	}

	mid := (end-begin)/2 + begin
	root := &TreeNode{
		Val: nums[mid],
	}

	root.Left = sortedArrayToBSTHelper(nums, begin, mid-1)
	root.Right = sortedArrayToBSTHelper(nums, mid+1, end)

	return root
}
