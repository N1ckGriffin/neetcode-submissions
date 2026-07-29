class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l, r = 0, 1
        chars = set(s[0])
        longest = 1

        while r < len(s):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            longest = max(longest, len(chars))
            r += 1
        
        return longest