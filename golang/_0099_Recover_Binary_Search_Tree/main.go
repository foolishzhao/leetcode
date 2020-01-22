package main

import "leetcode/golang/common"

type TreeNode = common.TreeNode

func recoverTree(root *TreeNode) {
	if root == nil {
		return
	}

	var firstPrev, firstCur, secondPrev, secondCur *TreeNode
	var prev *TreeNode
	for root != nil {
		if root.Left == nil {
			if prev != nil && prev.Val > root.Val {
				if firstPrev == nil {
					firstPrev, firstCur = prev, root
				} else {
					secondPrev, secondCur = prev, root
				}
			}

			prev = root
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
				if prev != nil && prev.Val > root.Val {
					if firstPrev == nil {
						firstPrev, firstCur = prev, root
					} else {
						secondPrev, secondCur = prev, root
					}
				}

				prev = root
				root = root.Right
			}
		}
	}

	if firstPrev != nil {
		if secondPrev != nil {
			firstPrev.Val, secondCur.Val = secondCur.Val, firstPrev.Val
		} else {
			firstPrev.Val, firstCur.Val = firstCur.Val, firstPrev.Val
		}
	}
}
