package main

import "leetcode/golang/common"

type TreeNode = common.TreeNode

func zigzagLevelOrder(root *TreeNode) [][]int {
	res := make([][]int, 0)
	if root != nil {
		queue := []*TreeNode{root}
		level := 1

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

			if level%2 == 0 {
				for i, j := 0, len(oneRes)-1; i < j; {
					oneRes[i], oneRes[j] = oneRes[j], oneRes[i]
					i++
					j--
				}
			}

			res = append(res, oneRes)
			level++
		}
	}

	return res
}
