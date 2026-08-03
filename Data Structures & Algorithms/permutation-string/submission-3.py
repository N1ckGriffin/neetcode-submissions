class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        charCounter = [0] * 26
        nonZeroes = 0
        
        for i in range(len(s1)):
            charCounter[ord(s1[i]) - ord('a')] -= 1
            charCounter[ord(s2[i]) - ord('a')] += 1
        
        for i in range (26):
            if charCounter[i] != 0:
                nonZeroes += 1
        
        if nonZeroes == 0:
            return True
        
        for i in range(len(s1), len(s2)):
            l = ord(s2[i - len(s1)]) - ord('a')
            r = ord(s2[i]) - ord('a')

            charCounter[l] -= 1

            if charCounter[l] == 0:
                nonZeroes -= 1
            elif charCounter[l] == -1:
                nonZeroes += 1

            charCounter[r] += 1
            
            if charCounter[r] == 0:
                nonZeroes -= 1
            elif charCounter[r] == 1:
                nonZeroes += 1

            if nonZeroes == 0:
                return True
        
        return False
