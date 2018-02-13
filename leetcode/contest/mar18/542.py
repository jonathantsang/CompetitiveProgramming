class Solution(object):
    
    rowN = 0
    elementN = 0
    
    def searchMatrix(self, matrix, elementRow, elementElement, height, width):
        min = height
        for rowNum in range(0, height):
            ## Break case too far from min
            if(min + elementRow < rowNum):
                return min
            calc = elementElement - min
            if(calc < 0):
                calc = 0
            for elementNum in range(calc, min):
                ## Break case too far from min
                if(min + elementElement < elementNum):
                    break
                if(elementNum >= width or elementRow >= height):
                    break
                if(matrix[rowNum][elementNum] == 0):
                    ## Check if the place is minimum
                    distance = abs(rowNum - elementRow) + abs(elementNum - elementElement)
                    if(distance < min):
                        min = distance
        return min
    
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        ## Number of rows
        height = len(matrix)
        ## Number of columns
        width = len(matrix[0])
        new = []
        for rowNum in range(0, height):
            new.append([])
            for elementNum in range(0, width):
                ## It is a zero
                if(matrix[rowNum][elementNum] == 0):
                    new[rowNum].append(0)
                ## It is a One, look for zero
                elif(matrix[rowNum][elementNum] == 1):
                    self.rowN = 0
                    self.elementN = 0
                    new[rowNum].append(self.searchMatrix(matrix, rowNum, elementNum, height, width))
        return new