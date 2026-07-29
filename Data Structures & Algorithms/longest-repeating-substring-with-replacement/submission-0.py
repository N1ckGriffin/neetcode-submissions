class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        currentLetters = defaultdict(int)
        res = 0

        for r in range(len(s)):
            currentLetters[s[r]] += 1
            
            wordLength = r - l + 1
            while wordLength - k - max(currentLetters.values()) > 0:
                currentLetters[s[l]] -= 1
                l += 1
                wordLength = r - l + 1

            res = max(res, wordLength)
        
        return res
