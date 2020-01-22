package main

import (
	"fmt"
	"strconv"
)

func getPermutation(n int, k int) string {
	res := ""

	nums := make([]int, n)
	for i := 0; i < n; i++ {
		nums[i] = i + 1
	}

	for ; n > 0; n-- {
		t := factorial(n - 1)
		pos := (k - 1) / t
		res += strconv.Itoa(nums[pos])
		nums = append(nums[:pos], nums[pos+1:]...)
		k = (k-1)%t + 1
	}

	return res
}

func factorial(n int) int {
	if n == 0 {
		return 1
	} else {
		return factorial(n-1) * n
	}
}

func main() {
	nums := []int{1, 2, 3}
	fmt.Println(nums[3:])
	fmt.Println(nums[:0])
}
