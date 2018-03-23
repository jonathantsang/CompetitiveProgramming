class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        lonely = 0
        picleng = len(picture)
        row = []
        column = []
        
        for w in range(0, 501):
            row.append(0)
        
        for w in range(0, 501):
            column.append(0)
        
        ## Find the number of B in the rows
        for j in range(0, picleng):
            leng = len(picture[j]);
            for i in range(0, leng):
                if(picture[j][i] == 'B'):
                    row[j] += 1
        
        ## Find the number of B in the columns
        for j in range(0, picleng):
            leng = len(picture[j]);
            for i in range(0, leng):
                if(picture[j][i] == 'B'):
                    column[i] += 1
        
        ## Go through all the rows and mark not lonely
        for j in range(0, picleng):
            leng = len(picture[j])
            for i in range(0, leng):
                ## If it is a B
                if('B' == picture[j][i]):
                    if(row[j] == 1 and column[i] == 1):
                        lonely += 1
        return lonely
                    