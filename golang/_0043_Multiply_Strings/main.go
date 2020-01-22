package main

import "strconv"

func multiply(num1 string, num2 string) string {
	m, n := len(num1), len(num2)

	nums := make([]int, m+n)
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			nums[i+j+1] += int(num1[i]-'0') * int(num2[j]-'0')
		}
	}

	for i := m + n - 1; i > 0; i-- {
		nums[i-1] += nums[i] / 10
		nums[i] %= 10
	}

	res, i := "", 0
	for ; i < m+n; i++ {
		if nums[i] > 0 {
			break
		}
	}

	if i == m+n {
		return "0"
	} else {
		for ; i < m+n; i++ {
			res += strconv.Itoa(nums[i])
		}

		return res
	}
}

func main() {
	multiply("123", "456")
}
