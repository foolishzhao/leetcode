class Solution:
    def evaluate(self, expression: str) -> int:
        tokens, var, st = [''], dict(), list()

        def eval_var(x):
            return var.get(x, x)

        def eval_token():
            if tokens[0] == 'add':
                return str(int(eval_var(tokens[1])) + int(eval_var(tokens[2])))
            elif tokens[0] == 'mult':
                return str(int(eval_var(tokens[1])) * int(eval_var(tokens[2])))
            else:
                for i in range(1, len(tokens) - 2, 2):
                    var[tokens[i]] = eval_var(tokens[i + 1])
                return eval_var(tokens[-1])

        for c in expression:
            if c == '(':
                if tokens[0] == 'let':
                    eval_token()
                st.append((tokens, dict(var)))
                tokens = ['']
            elif c == ')':
                token = eval_token()
                tokens, var = st.pop()
                tokens[-1] += token
            elif c == ' ':
                tokens.append('')
            else:
                tokens[-1] += c
        return int(tokens[0])


if __name__ == '__main__':
    Solution().evaluate("(let x 1 y 2 x (add x y) (add x y))")
