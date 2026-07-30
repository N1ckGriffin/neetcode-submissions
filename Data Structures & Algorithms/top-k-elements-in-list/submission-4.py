class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        buckets = [[] for i in range(len(nums) + 1)]

        for n, c in counts.items():
            buckets[c].append(n)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for j in range(len(buckets[i])):
                res.append(buckets[i][j])
                if len(res) == k:
                    return res