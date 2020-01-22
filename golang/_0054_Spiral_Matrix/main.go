package main

func spiralOrder(matrix [][]int) []int {
	if matrix == nil || len(matrix) == 0 || len(matrix[0]) == 0 {
		return []int{}
	}

	m, n := len(matrix), len(matrix[0])
	res := make([]int, 0, m*n)

	rb, re, cb, ce := 0, m-1, 0, n-1
	for rb <= re && cb <= ce {
		for k := cb; k <= ce; k++ {
			res = append(res, matrix[rb][k])
		}
		rb++

		for k := rb; k <= re; k++ {
			res = append(res, matrix[k][ce])
		}
		ce--

		if re >= rb {
			for k := ce; k >= cb; k-- {
				res = append(res, matrix[re][k])
			}
			re--
		}

		if cb <= ce {
			for k := re; k >= rb; k-- {
				res = append(res, matrix[k][cb])
			}
			cb++
		}
	}

	return res
}

func main() {
	matrix := [][]int{
		{2, 5, 8},
		{4, 0, -1},
	}
	spiralOrder(matrix)
}
