class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        m = 1

        for i in range(1, len(nums)):
            m *= nums[i - 1]
            output[i] *= m
        
        m = 1
        for i in range(len(nums) - 2, -1, -1):
            m *= nums[i + 1]
            output[i] *= m
        
        return output