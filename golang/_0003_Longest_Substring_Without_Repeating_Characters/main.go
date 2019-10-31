package main

import "fmt"

// suppose chars in s are within the ascii chars
func lengthOfLongestSubstring(s string) int {
	location := make([]int, 128)
	for i := 0; i < len(location); i++ {
		location[i] = -1
	}

	left, res := 0, 0
	for i, c := range s {
		if location[c] >= left {
			left = location[c] + 1
		} else if i-left+1 > res {
			res = i - left + 1
		}
		location[c] = i
	}

	return res
}

func lengthOfLongestSubstring2(s string) int {
	i, res := 0, 0
	runeMap := make(map[rune]int, len(s))

	for j, c := range s {
		if k, ok := runeMap[c]; ok && k >= i {
			if j-i > res {
				res = j - i
			}
			i = k + 1
		}
		runeMap[c] = j
	}

	if len(s)-i > res {
		res = len(s) - i
	}

	return res
}

func main() {
	fmt.Println(lengthOfLongestSubstring("abba"))
}
