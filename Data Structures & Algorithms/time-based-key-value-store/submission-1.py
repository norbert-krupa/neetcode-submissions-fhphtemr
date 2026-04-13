class TimeMap:

    def __init__(self):
        self.moodAtTime = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.moodAtTime:
            self.moodAtTime[key] = []
        
        self.moodAtTime[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        result = ""

        if key not in self.moodAtTime:
            return result

        left, right = 0, len(self.moodAtTime[key]) - 1

        while left <= right:
            mid = (left + right) // 2

            if self.moodAtTime[key][mid][0] <= timestamp:
                result = self.moodAtTime[key][mid][1]
                left = mid + 1
            elif self.moodAtTime[key][mid][0] > timestamp:
                right = mid - 1

        return result


