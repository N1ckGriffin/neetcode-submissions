class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in found:
                return found[diff], index
            found[num] = index
