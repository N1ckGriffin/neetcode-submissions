class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        tracked = {}
        maxLength, modeCount = 0, 0

        for r in range(len(s)):
            tracked[s[r]] = 1 + tracked.get(s[r], 0)
            modeCount = max(modeCount, tracked[s[r]])
            while (r - l + 1) - modeCount >  k:
                tracked[s[l]] -= 1
                l += 1
            maxLength = max(maxLength, r - l + 1)
        
        return maxLength
