class Solution:
    # Get row count
    # Then check rows if I turned my row (i) to all 0s or all 1s, see how that affects all other rows
    # Count them up
    
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        columns = len(matrix[0])
        
        best = 0
        
        rowindices = {} # Key: row index, Value: [[indices with 0][indices with 1]]
        for i in range(0, len(matrix)):
            rowindices[i] = [[],[]]
        rowvalues = [0 for i in range(0, rows)] # Each row has a certain number of 1s
        
        seen = {} # rows completed
        
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
                best += 1
                seen[i] = 1
        
        
        # want values of 0 all, or columns (meaning all 1s)
        for i in range(0, len(matrix)):
            
            if i in seen:
                continue
            
            newrow = rowvalues.copy()
            # If I turn all to 0s, flip the columns with 1
            for idx in rowindices[i][1]:
                for j in range(0, len(matrix)):
                    # matrix[j][idx] is being flipped
                    if matrix[j][idx] == 0:
                        newrow[j] +=1
                    else:
                        newrow[j] -= 1
            #print(newrow)
            res = 0
            for p, v in enumerate(newrow):
                if v == 0 or v == columns:
                    res += 1
                    seen[p] = 1
            
            best = max(best, res)
            
            newrow = rowvalues.copy()
            # If I turn all to 1s, flip the columns with 0
            for idx in rowindices[i][0]:
                for j in range(0, len(matrix)):
                    # matrix[j][idx] is being flipped
                    if matrix[j][idx] == 0:
                        newrow[j] += 1
                    else:
                        newrow[j] -= 1
            #print(newrow)
            res = 0
            for p, v in enumerate(newrow):
                if v == 0 or v == columns:
                    res += 1
                    seen[p] = 1
            
            best = max(best, res)
            #print(" ")
            
        return best