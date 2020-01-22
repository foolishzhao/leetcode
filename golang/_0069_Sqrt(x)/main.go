package main

func mySqrt(x int) int {
	if x == 0 || x == 1 {
		return x
	}

	left, right := uint64(1), uint64(x-1)
	for left <= right {
		mid := (right-left)/2 + left
		t := mid * mid
		if t == uint64(x) {
		return int(mid)
	} else if t < uint64(x) {
		left = mid + 1
	} else {
		right = mid - 1
	}
	}

	return int(right)
}
