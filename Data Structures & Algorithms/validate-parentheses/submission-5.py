class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openDict = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for c in s:
            if c in openDict:
                if stack and stack[-1] == openDict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack
                
