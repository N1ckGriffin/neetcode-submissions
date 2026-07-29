class Solution:
    def hammingWeight(self, n: int) -> int:
        output = 0
        while n:
            if n & 1:
                output += 1
            n >>= 1
        return output