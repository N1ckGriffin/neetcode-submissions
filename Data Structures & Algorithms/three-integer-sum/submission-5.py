class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for i in range(len(nums)):
            target = -nums[i]
            numToIndex = {}
            for j in range(len(nums)):
                if j != i:
                    diff = target - nums[j]
                    if diff in numToIndex:
                        triplet = tuple(sorted([nums[i], nums[j], nums[numToIndex[diff]]]))
                        result.add(triplet)
                    numToIndex[nums[j]] = j
        return list(list(t) for t in result)
