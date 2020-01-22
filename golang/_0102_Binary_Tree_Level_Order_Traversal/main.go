package main

import "leetcode/golang/common"

type TreeNode = common.TreeNode

func levelOrder(root *TreeNode) [][]int {
	res := make([][]int, 0)
	if root != nil {
		queue := []*TreeNode{root}
		for len(queue) > 0 {
			qLen := len(queue)
			oneRes := make([]int, 0)

			for i := 0; i < qLen; i++ {
				cur := queue[0]
				queue = queue[1:]

				if cur.Left != nil {
					queue = append(queue, cur.Left)
				}

				if cur.Right != nil {
					queue = append(queue, cur.Right)
				}

				oneRes = append(oneRes, cur.Val)
			}

			res = append(res, oneRes)
		}
	}

	return res
}
