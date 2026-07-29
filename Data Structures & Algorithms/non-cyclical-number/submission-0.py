class Solution:
    def isHappy(self, n: int) -> bool:
        found = set()

        while True:
            if n == 1:
                return True
            if n in found:
                return False
            found.add(n)
            n = self.sumOfSquares(n)
            

    def sumOfSquares(self, n: int) -> int:
        output = 0
        while n != 0:
            ones = n % 10
            output += ones**2
            n //= 10
        
        return output
