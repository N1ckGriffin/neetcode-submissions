class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charDict = {}
        for character in s:
            if character not in charDict:
                charDict[character] = 1
            else:
                charDict[character] += 1
        
        for character in t:
            if character not in charDict:
                return False
            else:
                charDict[character] -= 1
                if charDict[character] == 0:
                    del charDict[character]
        
        return len(charDict) == 0

                