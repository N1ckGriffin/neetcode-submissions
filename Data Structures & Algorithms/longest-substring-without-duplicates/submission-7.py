class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        front = 0
        inSubstring = set()
        res = 0

        for back in range(len(s)):
            while s[back] in inSubstring:
                inSubstring.remove(s[front])
                front += 1
            res = max(res, back - front + 1)
            inSubstring.add(s[back])
        
        return res

            
            