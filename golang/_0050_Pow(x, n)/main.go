package main

import "math"

func myPow(x float64, n int) float64 {
	if math.Abs(x) < 1e-6 {
		return 0
	} else if n == 0 {
		return 1
	} else if n == 1 {
		return x
	} else if n < 0 {
		return myPow(float64(1)/x, -n)
	}

	t := myPow(x, n>>1)
	if n%2 == 0 {
		return t * t
	} else {
		return t * t * x
	}
}
