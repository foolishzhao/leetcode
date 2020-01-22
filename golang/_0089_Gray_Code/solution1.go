package main

func grayCode(n int) []int {
	res := make([]int, 0, 1<<uint32(n))
	res = append(res, 0)
	for i := 0; i < n; i++ {
		t := 1 << uint32(i)
		for j := len(res) - 1; j >= 0; j-- {
			res = append(res, res[j]+t)
		}
	}

	return res
}
