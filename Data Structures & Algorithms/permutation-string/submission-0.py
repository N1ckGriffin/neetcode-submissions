class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = Counter(s1)
        l = 0

        for r in range(len(s2)):
            if s2[r] in counts:
                counts[s2[r]] -= 1
                while (counts[s2[r]] < 0):
                    counts[s2[l]] += 1
                    l += 1
                if r - l + 1 == len(s1):
                    return True
            else:
                while l < r:
                    counts[s2[l]] += 1
                    l += 1
                l += 1
        
        return False