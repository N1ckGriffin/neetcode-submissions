class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        foo = set()
        for n in nums:
            if n in foo:
                return True
            foo.add(n)
        return False