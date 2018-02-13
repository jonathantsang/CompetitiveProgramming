class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max = 0
        for i in range(0, len(heights)):
            number = 0
            end = i
            start = i
            ind = i + 1
            while(ind < len(heights)):
                if(heights[ind] >= heights[i]):
                    end = end + 1
                else:
                    break
                ind = ind + 1
            ind = i - 1
            while(ind > -1):
                if(heights[ind] >= heights[i]):
                    start = start - 1
                else:
                    break
                ind = ind - 1
            area = ((end - start) + 1) * heights[i]
            if(area > max):
                max = area
        return max