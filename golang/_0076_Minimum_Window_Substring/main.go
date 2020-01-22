package main

func minWindow(s string, t string) string {
	sLen, tLen := len(s), len(t)
	if sLen < tLen {
		return ""
	}

	var res string
	var minLen = sLen + 1

	tMap := make(map[byte]int, 0)
	for i := range t {
		tMap[t[i]]++
	}

	i, j, matchCnt := 0, 0, 0
	sMap := make(map[byte]int, 0)
	for ; j < sLen; j++ {
		c := s[j]
		sMap[c]++
		if v, ok := tMap[c]; ok && v >= sMap[c] {
			matchCnt++
		}

		if matchCnt == tLen {
			for ; i < sLen; i++ {
				c = s[i]
				sMap[c]--
				if v, ok := tMap[c]; ok && v > sMap[c] {
					matchCnt--
					break
				}
			}

			if j-i+1 < minLen {
				minLen = j - i + 1
				res = s[i : j+1]
			}

			i++
		}
	}

	return res
}

func minWindow2(s string, t string) string {
	sLen, tLen := len(s), len(t)
	if sLen < tLen {
		return ""
	}

	var res string
	var minLen = sLen + 1

	tMap := make(map[byte]int, 0)
	for i := range t {
		tMap[t[i]]++
	}

	matchCnt := 0
	for i, j := 0, 0; j < sLen; j++ {
		c := s[j]
		tMap[c]--
		if tMap[c] >= 0 {
			matchCnt++
		}

		if matchCnt == tLen {
			for ; i < sLen; i++ {
				c = s[i]
				tMap[c]++
				if tMap[c] > 0 {
					matchCnt--
					break
				}
			}

			if j-i+1 < minLen {
				minLen = j - i + 1
				res = s[i : j+1]
			}

			i++
		}
	}

	return res
}

func main() {
	minWindow("ADOBECODEBANC", "ABC")
}
