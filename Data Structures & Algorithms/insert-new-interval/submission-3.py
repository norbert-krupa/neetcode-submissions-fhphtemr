class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        len_intervals = len(intervals)
        result = []
        newIntervalAdded = False

        for i in range(len_intervals):
            
            if newIntervalAdded or intervals[i][1] < newInterval[0]:
                result.append(intervals[i])
            elif intervals[i][0] > newInterval[1]:
                result.append(newInterval)
                newIntervalAdded = True
                result.append(intervals[i])
            elif intervals[i][1] >= newInterval[0]:
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])

        if not newIntervalAdded:
            result.append(newInterval)

        return result