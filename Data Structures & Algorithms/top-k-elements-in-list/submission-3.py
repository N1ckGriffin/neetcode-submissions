class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        heap = [(v, k) for k, v in counts.items()]
        heapq.heapify(heap)

        return [n for count, n in heapq.nlargest(k, heap)]