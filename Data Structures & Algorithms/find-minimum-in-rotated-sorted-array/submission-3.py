class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0 , len(nums) - 1

        while l != r:
            m = l + (r - l) // 2

            if nums[l] > nums[r] and nums[m] > nums[r]:
                l = m + 1
            elif nums[l] > nums[r]:
                r = m
            else:
                return nums[l]
        
        return nums[l]

