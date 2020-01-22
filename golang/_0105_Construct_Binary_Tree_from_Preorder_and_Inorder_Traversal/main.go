package main

import "leetcode/golang/common"

type TreeNode = common.TreeNode

func buildTree(preorder []int, inorder []int) *TreeNode {
	if len(preorder) != len(inorder) {
		return nil
	}

	n := len(preorder)
	return buildTreeHelper(preorder, 0, n-1, inorder, 0, n-1)
}

func buildTreeHelper(prevorder []int, b1, e1 int, inorder []int, b2, e2 int) *TreeNode {
	if b1 > e1 {
		return nil
	}

	root := &TreeNode{
		Val: prevorder[b1],
	}

	i := b2
	for ; i <= e2 && inorder[i] != prevorder[b1]; i++ {
	}

	root.Left = buildTreeHelper(prevorder, b1+1, i-b2+b1, inorder, b2, i-1)
	root.Right = buildTreeHelper(prevorder, i+1-e2+e1, e1, inorder, i+1, e2)

	return root
}
