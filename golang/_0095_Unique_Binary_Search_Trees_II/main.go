package main

import "leetcode/golang/common"

type TreeNode = common.TreeNode

func generateTrees(n int) []*TreeNode {
	if n == 0 {
		return []*TreeNode{}
	}
	return dfs(1, n)
}

func dfs(start, end int) []*TreeNode {
	res := make([]*TreeNode, 0)
	if start <= end {
		for i := start; i <= end; i++ {
			left := dfs(start, i-1)
			right := dfs(i+1, end)

			for u := range left {
				for v := range right {
					root := &TreeNode{
						Val:   i,
						Left:  left[u],
						Right: right[v],
					}
					res = append(res, root)
				}
			}
		}
	} else {
		res = append(res, nil)
	}

	return res
}
