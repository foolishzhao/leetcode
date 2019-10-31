package main

func romanToInt(s string) int {
	mp := map[byte]int{
		'M': 1000,
		'D': 500,
		'C': 100,
		'L': 50,
		'X': 10,
		'V': 5,
		'I': 1,
	}

	res, n := 0, len(s)
	for i := 0; i < n; i++ {
		if i == n-1 || mp[s[i]] >= mp[s[i+1]] {
			res += mp[s[i]]
		} else {
			res -= mp[s[i]]
		}
	}

	return res
}
