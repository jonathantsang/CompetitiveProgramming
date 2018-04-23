class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if(len(heights) < 1):
            return 0
        if(len(heights) < 2):
            return heights[0]
        maxsofar = max(heights[0], heights[1])
        secondmaxsofar = min(heights[0],heights[1])
        for i in range(0, len(heights)-1):
            ## Check to see if curr is greater than next
            if heights[i] > heights[i + 1]:
                ## If the smaller is greater than the secondmaxsofar
                if heights[i + 1] > secondmaxsofar:
                    ## Change the values
                    maxsofar = heights[i]
                    secondmaxsofar = heights[i + 1]
            elif heights[i + 1] >= heights[i]:
                ## If the smaller is greater than the secondmaxsofar
                if heights[i] > secondmaxsofar:
                    ## Change the values
                    maxsofar = heights[i + 1]
                    secondmaxsofar = heights[i]
        return secondmaxsofar * 2