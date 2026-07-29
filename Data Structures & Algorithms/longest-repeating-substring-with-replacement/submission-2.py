class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        countsMax = 0
        longest = 0
        l = 0

        for r in range(len(s)):
            counts[s[r]] += 1
            countsMax = max(countsMax, counts[s[r]])

            while (r - l + 1) - countsMax > k:
                counts[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        
        return longest
            
        

