class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse = True)
        prevTime = (target - pairs[0][0]) / pairs[0][1]
        fleets = 1
        
        for p, s in pairs:
            currTime = (target - p) / s
            if currTime > prevTime:
                fleets += 1
                prevTime = currTime

        return fleets
