class Solution:
    def isValid(self, s: str) -> bool:
        closingToOpening = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        stack = []
        
        for c in s:
            if c in closingToOpening:
                if len(stack) == 0:
                    return False
                if closingToOpening[c] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0