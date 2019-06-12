class Solution:
    # Get row count
    # Then check rows if I turned my row (i) to all 0s or all 1s, see how that affects all other rows
    # Count them up
    def oppositenum(self, numstr):
        ans = ""
        for c in numstr:
            if c == "0":
                ans += "1"
            else:
                ans += "0"
        return ans
    
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        columns = len(matrix[0])
        
        best = 0
        base = 0
        
        rowindices = {} # Key: row index, Value: [[indices with 0][indices with 1]]
        for i in range(0, len(matrix)):
            rowindices[i] = [[],[]]
        rowvalues = [0 for i in range(0, rows)] # Each row has a certain number of 1s
                
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                # print(i, j)
                rowvalues[i] += matrix[i][j]
                if matrix[i][j] == 0:
                    rowindices[i][0].append(j)
                else:
                    rowindices[i][1].append(j)
        #print(rowvalues)
        #print(rowindices)
        # Count no flip rowvalues
        for i, v in enumerate(rowvalues):
            if v == 0 or v == columns:
                base += 1
        best = base
      
        # array as keys
        formula = {} # Key: array values as num, Value: number seen
        # 101 and 010 added to best when flipped
        for row in matrix:
            res = "".join(map(str, row))
            if res not in formula:
                formula[res] = 1
            else:
                formula[res] += 1
                
        for value in formula:
            added = formula[value]
            # Get the opposite binary number
            opposite = self.oppositenum(value)
            if opposite in formula:
                added += formula[opposite]
            best = max(best, added)
            
        return best