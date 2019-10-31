package main

import (
	"math"
)

func myAtoi(str string) int {
	i, n, sign, res := 0, len(str), int64(1), int64(0)

	for i < n && str[i] == ' ' {
		i++
	}

	if i < n && (str[i] == '-' || str[i] == '+') {
		if str[i] == '-' {
			sign = -1
		}
		i++
	}

	for i < n && str[i] >= '0' && str[i] <= '9' {
		res = res*10 + int64(str[i]-'0')
		i++

		if sign*res < math.MinInt32 {
			return math.MinInt32
		} else if sign*res > math.MaxInt32 {
			return math.MaxInt32
		}
	}

	return int(sign * res)
}
