package main

import "fmt"

func findSubstring(s string, words []string) []int {
	sLen, wLen, res := len(s), len(words), make([]int, 0)
	if wLen == 0 || wLen*len(words[0]) > sLen {
		return res
	}

	wwLen, wordMap := len(words[0]), make(map[string]int, wLen)
	for _, w := range words {
		wordMap[w]++
	}

	for i := 0; i <= sLen-wLen*wwLen; i++ {
		mp := make(map[string]int, len(wordMap))
		for k, v := range wordMap {
			mp[k] = v
		}

		j := i
		for ; j < i+wLen*wwLen; j += wwLen {
			str := s[j : j+wwLen]
			mp[str]--
			if mp[str] < 0 {
				break
			}
		}

		if j == i+wLen*wwLen {
			res = append(res, i)
		}
	}

	return res
}

func main() {
	wordMap := make(map[string]int, 5)
	wordMap["hello"]++

	fmt.Println(wordMap)

	findSubstring("barfoothefoobarman", []string{"foo", "bar"})
}
