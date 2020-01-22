package main

import "leetcode/golang/common"

type TreeNode = common.TreeNode

func isSymmetric(root *TreeNode) bool {
	return isSymmetricHelper(root, root)
}

func isSymmetricHelper(left, right *TreeNode) bool {
	if left == nil && right == nil {
		return true
	} else if left == nil || right == nil {
		return false
	} else {
		return left.Val == right.Val &&
			isSymmetricHelper(left.Left, right.Right) &&
			isSymmetricHelper(left.Right, right.Left)
	}
}

func isSymmetric2(root *TreeNode) bool {
	if root == nil {
		return true
	}

	queue := []*TreeNode{root}
	for len(queue) > 0 {
		qLen := len(queue)
		vals := make([]*int, 0)

		for i := 0; i < qLen; i++ {
			cur := queue[0]
			queue = queue[1:]

			if cur.Left != nil {
				queue = append(queue, cur.Left)
				vals = append(vals, &cur.Left.Val)
			} else {
				vals = append(vals, nil)
			}

			if cur.Right != nil {
				queue = append(queue, cur.Right)
				vals = append(vals, &cur.Right.Val)
			} else {
				vals = append(vals, nil)
			}
		}

		for i, j := 0, len(vals)-1; i < j; {
			if vals[i] == nil && vals[j] == nil {

			} else if vals[i] == nil || vals[j] == nil {
				return false
			} else if *vals[i] != *vals[j] {
				return false
			}

			i++
			j--
		}
	}

	return true
}
