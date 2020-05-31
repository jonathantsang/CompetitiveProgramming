class Solution:
    def solve(self, s, k):
        places = []
        for i, v in enumerate(s):
            if v == 'x':
                places.append(i)

        intervals = []
        for p in places:
            intervals.append([p-k+1, p+k-1])
        print(intervals)

        # check intervals if they are disjoint for a number
        pos = 0
        for intv in intervals:
            if pos >= intv[0] and pos <= intv[1]:
                pos = intv[1]+1
            else:
                return True
        if pos < len(s):
            return True
        return False
