class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []

        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        
        res = [-heap[0][0]]
        l, r = 0, k - 1

        while r < len(nums) - 1:
            l, r = l + 1, r + 1
            while heap and heap[0][1] < l:
                heapq.heappop(heap)
            heapq.heappush(heap, (-nums[r], r))
            res.append(-heap[0][0])
        
        return res