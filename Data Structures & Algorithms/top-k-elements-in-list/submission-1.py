class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        freq = [[] for i in range(len(nums))]
        for n, c in counts.items():
            freq[c - 1].append(n)  
        
        res = []
        for i in range(len(freq)- 1, -1, -1):
            if len(freq[i]) > 0:
                for value in freq[i]:
                    res.append(value)
                    if len(res) == k:
                        return res