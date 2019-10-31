package main

import "leetcode/golang/common"

type ListNode = common.ListNode

type PQ []*ListNode

func (pq *PQ) swap(i, j int) {
	(*pq)[i], (*pq)[j] = (*pq)[j], (*pq)[i]
}

func (pq *PQ) less(i, j int) bool {
	return (*pq)[i].Val < (*pq)[j].Val
}

func (pq *PQ) adjustUp(i int) {
	for i > 0 {
		j := (i - 1) / 2
		if pq.less(i, j) {
			pq.swap(i, j)
			i = j
		} else {
			break
		}
	}
}

func (pq *PQ) adjustDown(i, n int) {
	for 2*i+1 < n {
		j := 2*i + 1
		if j+1 < n && pq.less(j+1, j) {
			j++
		}

		if pq.less(j, i) {
			pq.swap(i, j)
			i = j
		} else {
			break
		}
	}
}

func (pq *PQ) Push(node *ListNode) bool {
	if node == nil {
		return false
	}

	*pq = append(*pq, node)
	pq.adjustUp(len(*pq) - 1)

	return true
}

func (pq *PQ) Pop() *ListNode {
	if pq.IsEmpty() {
		return nil
	}

	n := len(*pq)

	pq.swap(0, n-1)
	pq.adjustDown(0, n-1)

	res := (*pq)[n-1]
	*pq = (*pq)[:n-1]

	return res
}

func (pq *PQ) IsEmpty() bool {
	return len(*pq) == 0
}

func mergeKLists(lists []*ListNode) *ListNode {
	dummy := new(ListNode)
	tail := dummy

	pq := make(PQ, 0, len(lists))
	for _, v := range lists {
		pq.Push(v)
	}

	for !pq.IsEmpty() {
		node := pq.Pop()
		tail.Next = node
		tail = tail.Next

		if node.Next != nil {
			pq.Push(node.Next)
		}
	}

	tail.Next = nil
	return dummy.Next
}
