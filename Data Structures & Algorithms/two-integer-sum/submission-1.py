class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in dict:
                return [dict[diff], index]
            dict[value] = index