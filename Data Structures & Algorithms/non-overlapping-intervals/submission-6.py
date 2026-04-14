class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort()
        smallEnd = intervals[0][1]

        for i in range(len(intervals) - 1):
            if smallEnd > intervals[i+1][0]:
                smallEnd = min(smallEnd, intervals[i+1][1])
                count += 1
            else:
                smallEnd = intervals[i+1][1]

        return count



        