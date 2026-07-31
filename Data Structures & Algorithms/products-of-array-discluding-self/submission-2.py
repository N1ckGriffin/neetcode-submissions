class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        product = 1
        for i in range(len(nums) - 1):
            product *= nums[i]
            res[i + 1] *= product
        
        product = 1
        for i in range(len(nums) - 1, 0, -1):
            product *= nums[i]
            res[i - 1] *= product

        return res