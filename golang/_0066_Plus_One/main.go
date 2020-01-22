package main

import "fmt"

func plusOne(digits []int) []int {
	carry := 1
	for i := len(digits) - 1; i >= 0; i-- {
		t := digits[i] + carry
		carry = t / 10
		digits[i] = t % 10
	}

	if carry > 0 {
		digits = append([]int{carry}, digits...)
	}

	return digits
}

func main() {
	var digits []int
	fmt.Println(append([]int{1}, digits...))
}