class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        N,M=len(matrix),len(matrix[0])
        ymin=-1
        ymax=N
        xmin=-1
        xmax=M
        ans = []
        y=0
        x=0
        d = 1 # 0 up, 1 right, 2 down, 3 left
        c = 0
        count = sum(len(r) for r in matrix)
        while(c < count):
            # add value
            ans.append(matrix[y][x])
            c+=1
            
            if d == 0:
                y-=1
            elif d == 1:
                x+=1
            elif d == 2:
                y+=1
            elif d == 3:
                x-=1
            
            if x == xmax:
                # go down
                d = (d+1)%4
                ymin+=1
                y+=1
                x-=1
                continue
                
            elif x == xmin:
                # go up
                d = (d+1)%4
                ymax-=1
                y-=1
                x+=1
                continue
                
            elif y == ymin:
                # go right
                d = (d+1)%4
                xmin+=1
                x+=1
                y+=1
                continue
                
            elif y == ymax:
                # go left
                d = (d+1)%4
                xmax-=1
                x -= 1
                y-=1
                continue
        
        return ans
