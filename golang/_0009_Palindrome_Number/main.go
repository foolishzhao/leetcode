package main

func isPalindrome(x int) bool {
	if x == 0 {
		return true
	} else if x < 0 || x%10 == 0 {
		return false
	}

	rx := 0
	for x > rx {
		if x/10 == rx {
			break
		}
		rx = rx*10 + x%10
		x /= 10
	}

	return x == rx || x/10 == rx
}
