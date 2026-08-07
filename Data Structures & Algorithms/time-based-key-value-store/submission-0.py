class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.map[key]) - 1
        res = ""

        while l <= r:
            m = l + (r - l) // 2
            if self.map[key][m][0] <= timestamp:
                res = self.map[key][m][1]
                l = m + 1
            else:
                r = m - 1
        
        return res

