class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        working_interval = intervals[0]
        result = []
        len_intervals = len(intervals)

        for i in range(len_intervals):
            if i == len_intervals - 1:
                result.append(working_interval)
            elif working_interval[1] >= intervals[i+1][0]:
                    working_interval[1] = max(working_interval[1], intervals[i+1][1])
            else:
                result.append(working_interval)
                working_interval = intervals[i+1]

        return result
                


