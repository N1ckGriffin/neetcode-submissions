class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letters1 = {}
        letters2 = {}
        for i in range(len(s)):
            if s[i] not in letters1:
                letters1[s[i]] = 1
            else:
                letters1[s[i]] += 1
            if t[i] not in letters2:
                letters2[t[i]] = 1
            else:
                letters2[t[i]] += 1
        return letters1 == letters2


                