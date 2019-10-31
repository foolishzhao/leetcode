package main

import (
	"math"
)

func divide(dividend int, divisor int) int {
	sign := 1
	if (dividend^divisor)>>31 != 0 {
		sign = -1
	}

	dividend, divisor, res := abs(dividend), abs(divisor), 0
	for dividend >= divisor {
		shift := uint32(1)
		for (divisor << shift) < dividend {
			shift++
		}

		dividend -= divisor << (shift - 1)
		res += 1 << (shift - 1)
	}

	if res*sign > math.MaxInt32 {
		return math.MaxInt32
	} else {
		return res * sign
	}
}

func abs(x int) int {
	if x < 0 {
		return -x
	}

	return x
}

func main() {
	divide(7, -3)
}
