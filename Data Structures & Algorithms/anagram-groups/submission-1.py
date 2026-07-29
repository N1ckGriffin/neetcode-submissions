class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        for s in strs:
            found = False
            for subList in result:
                if Counter(s) == Counter(subList[0]):
                    subList.append(s)
                    found = True
                    break
            if not found:
                result.append([s])
        return result
