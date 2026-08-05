class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for s in tokens:
            match s:
                case '+':
                    operand2, operand1 = stack.pop(), stack.pop()
                    stack.append(operand1 + operand2)
                case '-':
                    operand2, operand1 = stack.pop(), stack.pop()
                    stack.append(operand1 - operand2)
                case '*':
                    operand2, operand1 = stack.pop(), stack.pop()
                    stack.append(operand1 * operand2)
                case '/':
                    operand2, operand1 = stack.pop(), stack.pop()
                    stack.append(int(operand1 / operand2))
                case _:
                    stack.append(int(s))
        
        return stack[0]

                