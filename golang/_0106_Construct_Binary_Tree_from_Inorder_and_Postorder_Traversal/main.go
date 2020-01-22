package main

import "leetcode/golang/common"

type TreeNode = common.TreeNode

func buildTree(inorder []int, postorder []int) *TreeNode {
	if len(inorder) != len(postorder) {
		return nil
	}

	n := len(inorder)
	return buildTreeHelper(inorder, 0, n-1, postorder, 0, n-1)
}

func buildTreeHelper(inorder []int, b1, e1 int, postorder []int, b2, e2 int) *TreeNode {
	if b1 > e1 {
		return nil
	}

	root := &TreeNode{
		Val: postorder[e2],
	}

	i := b1
	for ; i <= e1 && inorder[i] != postorder[e2]; i++ {
	}

	root.Left = buildTreeHelper(inorder, b1, i-1, postorder, b2, i-1-b1+b2)
	root.Right = buildTreeHelper(inorder, i+1, e1, postorder, i-e1+e2, e2-1)

	return root
}
