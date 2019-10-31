package main

import (
	"fmt"
	"math"
	"math/bits"
)

// int/uint is 32 bit on 32-bit cpu, 64 bit on 64-bit machine
func reverse(x int) int {
	sign, xx, res := 1, int64(x), int64(0)
	if x < 0 {
		sign = -1
		xx = -xx
	}

	for xx > 0 {
		res = res*10 + xx%10
		xx /= 10

		if res > math.MaxInt32 {
			return 0
		}
	}

	return sign * int(res)
}

func main() {
	fmt.Println(bits.UintSize)
}
