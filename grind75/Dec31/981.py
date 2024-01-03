from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        for i in range(len(self.d[key])-1, -1, -1):
            if self.d[key][i][0] <= timestamp:
                return self.d[key][i][1]
        
        return ""

