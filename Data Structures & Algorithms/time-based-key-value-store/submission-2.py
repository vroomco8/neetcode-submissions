class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key] = self.hashmap.get(key, []) + [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.hashmap.get(key, [])) - 1

        res = ""
        while l <= r:
            mid = (l + r) // 2
            curTime = self.hashmap[key][mid][0]
            if curTime == timestamp:
                res = self.hashmap[key][mid][1]
                break
            elif curTime < timestamp:
                res = self.hashmap[key][mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res

        
