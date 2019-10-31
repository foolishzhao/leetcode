package main

func isValid(s string) bool {
	n := len(s)

	stack, top := make([]byte, n), 0
	for _, b := range s { // b is of type int32
		switch b {
		case '(':
			stack[top] = ')'
			top++
		case '[':
			stack[top] = ']'
			top++
		case '{':
			stack[top] = '}'
			top++
		case ')', ']', '}':
			if top == 0 || stack[top-1] != byte(b) {
				return false
			}

			top--
		}
	}

	return top == 0
}

func main() {
	isValid("()")
}
