class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = 0
        for pile in piles:
            maxPile = max(maxPile, pile)
        l, r = 1, maxPile
        minK = maxPile
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile) / k)
            if hours <= h:
                minK = min(minK, k)
                r = k - 1
            else:
                l = k + 1
        return minK
            