package main

func generateMatrix(n int) [][]int {
	res := make([][]int, n)
	for i := 0; i < n; i++ {
		res[i] = make([]int, n)
	}

	rowTop, rowBottom := 0, n-1
	colLeft, colRight := 0, n-1
	k := 1

	for rowTop <= rowBottom && colLeft <= colRight {
		for i := colLeft; i <= colRight; i++ {
			res[rowTop][i] = k
			k++
		}
		rowTop++

		for i := rowTop; i <= rowBottom; i++ {
			res[i][colRight] = k
			k++
		}
		colRight--

		if rowTop <= rowBottom {
			for i := colRight; i >= colLeft; i-- {
				res[rowBottom][i] = k
				k++
			}
			rowBottom--
		}

		if colLeft <= colRight {
			for i := rowBottom; i >= rowTop; i-- {
				res[i][colLeft] = k
				k++
			}
			colLeft++
		}
	}

	return res
}
