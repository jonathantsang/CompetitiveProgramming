class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        totals = []
        
        ## Convert each time to minutes
        for time in timePoints:
            timeHoursAndMins = time.split(":")
            totalMins = int(timeHoursAndMins[0]) * 60 + int(timeHoursAndMins[1])
            totals.append(totalMins)
        
        ## Sort the times
        totals.sort()
        leng = len(totals)
        
        mini = totals[1] - totals[0]
        ## Check the overflow answer
        checkOverflow = min(abs(totals[leng -1] - totals[0]), \
                            (1440 - totals[leng-1]) + totals[0])
        if(mini > checkOverflow):
            mini = checkOverflow
        for i in range(2, leng):
            calc = totals[i] - totals[i-1]
            if(calc < mini):
                mini = calc
        return mini
            