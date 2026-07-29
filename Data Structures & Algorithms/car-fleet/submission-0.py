class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

            pairs = [(p, s) for p, s in zip(position, speed)]
            pairs.sort(reverse = True)

            result = 0
            current = 0

            for p, s in pairs:
                time = float(target - p) / s

                if time > current:
                    result += 1
                    current = time

            return result 