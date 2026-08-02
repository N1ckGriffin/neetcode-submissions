class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        front = 0
        inSubstring = set()
        res = 0

        for back in range(len(s)):
            if s[back] in inSubstring:
                while s[front] != s[back]:
                    inSubstring.remove(s[front])
                    front += 1
                inSubstring.remove(s[front])
                front += 1
            length = back - front + 1
            res = max(res, length)
            inSubstring.add(s[back])
        
        return res

            
            