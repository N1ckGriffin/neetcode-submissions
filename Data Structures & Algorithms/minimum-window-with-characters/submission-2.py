class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts = Counter(t)
        l = 0
        while l < len(s) and s[l] not in counts:
            l += 1
        totalCount = len(t)
        res = ""

        for r in range(l, len(s)):
            if s[r] in counts and totalCount > 0:
                counts[s[r]] -= 1
                if counts[s[r]] >= 0:
                    totalCount -= 1

            if totalCount == 0:
                while totalCount == 0:
                    if s[l] in counts:
                        counts[s[l]] += 1
                        if counts[s[l]] > 0:
                            totalCount += 1
                    l += 1
                if res == "" or r - l + 2 < len(res):
                    res = s[l - 1: r + 1]
                    
        return res

                