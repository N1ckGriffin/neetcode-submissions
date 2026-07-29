class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        heap = [(-1 * value, key) for key, value in counts.items()]
        heapq.heapify(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res