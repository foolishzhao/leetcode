package main

func strStr(haystack string, needle string) int {
	m, n := len(haystack), len(needle)
	if n == 0 {
		return 0
	} else if m < n {
		return -1
	}

	next := getNext(needle)
	i, j := 0, 0
	for i < m {
		if haystack[i] == needle[j] {
			i++
			j++
			if j == n {
				return i - n
			}
		} else if j > 0 {
			j = next[j]
		} else {
			i++
		}
	}

	return -1
}

// mathematical induction

// arr: 0, 1, 2, ..., i-1, ..., j-1, j
// next[j]: arr[0:j-1] is consistent with haystack, but arr[j] not, the next index of needle to compare.
// next[j] = i, arr[0:i-1] = arr[j-i:j-1]
// special case: next[0] = next[1] = 0
func getNext(str string) []int {
	i, j, n := 0, 1, len(str)
	next := make([]int, n+1)
	for ; j < n; {
		if str[i] == str[j] {
			i++
			j++
			next[j] = i
		} else if i > 0 {
			i = next[i]
		} else {
			j++
		}
	}

	return next
}

func main() {
	strStr("hello", "ll")
}
