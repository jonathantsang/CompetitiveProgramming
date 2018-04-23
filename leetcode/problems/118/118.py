class Solution(object):
    
    def newRow(self, lastrow):
        row = [lastrow[0]]
        for i in range(1, len(lastrow)):
            if(i == len(lastrow) - 1):
                row.append(lastrow[i])
            else:
                row.append(lastrow[i] + lastrow[i + 1])
        return row
    
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pt = []
        lastrow = []
        if(numRows < 1):
            return pt
        elif(numRows >= 1):
            pt.append([1])
            lastrow = [1]
            numRows -= 1
        if(numRows >= 1):
            pt.append([1,1])
            lastrow = [1,1]
            numRows -= 1
        while(numRows > 0):
            row = self.newRow(lastrow)
            pt.append(row)
        return pt