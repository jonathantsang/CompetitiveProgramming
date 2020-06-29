class Solution:
    def solve(self, intervals):
        if not intervals: return 0
        if len(intervals) == 1:
            return 0
        intervals.sort()

        merged = []
        for interval in intervals:
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        if len(merged) == 1:
            return 0

        return merged[-1][0] - merged[0][1]
