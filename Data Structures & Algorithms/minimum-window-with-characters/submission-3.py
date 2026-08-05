class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = {}
        for c in t:
            tCount[c] = 1 + tCount.get(c, 0)
        
        matches = 0
        res = ""

        l = 0
        for r in range(len(s)):
            if s[r] in tCount:
                tCount[s[r]] -= 1
                if tCount[s[r]] == 0:
                    matches += 1
            
            while matches == len(tCount):
                if s[l] in tCount and tCount[s[l]] == 0:
                    if not res or r - l + 1 < len(res):
                        res = s[l:r+1]
                    break
                elif s[l] in tCount:
                    tCount[s[l]] += 1
                l += 1
        
        return res



            

        

            
            


 