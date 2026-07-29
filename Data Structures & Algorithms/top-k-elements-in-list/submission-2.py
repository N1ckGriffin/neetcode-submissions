class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = defaultdict(int)
        for n in nums:
            countDict[n] += 1
        
        buckets = [[] for i in range(len(nums) + 1)]
        for n, count in countDict.items():
            buckets[count].append(n)
        
        result = []
        for i in range(len(nums), 0, -1):
            for n in buckets[i]:
                result.append(n)
                if len(result) == k:
                    return result