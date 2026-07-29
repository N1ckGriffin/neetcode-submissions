class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            match token:
                case '+':
                    var1 = stack.pop()
                    var2 = stack.pop()
                    stack.append(var1 + var2)
                case '-':
                    var1 = stack.pop()
                    var2 = stack.pop()
                    stack.append(var2 - var1)
                case '*':
                    var1 = stack.pop()
                    var2 = stack.pop()
                    stack.append(var1 * var2)
                case '/':
                    var1 = stack.pop()
                    var2 = stack.pop()
                    stack.append(int(float(var2) / var1))
                case _:
                    stack.append(int(token))
        return stack.pop()