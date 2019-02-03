class Solution(object):
    phone = [[1,2,3],
             [4,5,6],
             [7,8,9],
             [-1, 0, -1]]
    modulo = 10000000000 + 7
    seen = dict()
    
    def traverse(self, x, y, hops, number):
        xMax = 2
        yMax = 3
        
        if hops == 0:
            self.seen[number] = 1
            return
        ## Hop directions
        
        ## up 2, left 1
        if ( x - 1 >= 0 and y - 2 >= 0 and self.phone[y-2][x-1] != -1):
            self.traverse(x-1, y-2, hops-1, number+str(self.phone[y-2][x-1]))
        ## up 2, right 1
        if ( x + 1 <= xMax and y - 2 >= 0 and self.phone[y-2][x+1] != -1):
            self.traverse(x+1, y-2, hops-1, number+str(self.phone[y-2][x+1]))
        ## right 2, up 1
        if ( x + 2 <= xMax and y - 1 >= 0 and self.phone[y-1][x+2] != -1):
            self.traverse(x+2, y-1, hops-1, number+str(self.phone[y-1][x+2]))
        ## right 2, down 1
        if ( x + 2 <= xMax and y + 1 <= yMax and self.phone[y+1][x+2] != -1):
            self.traverse(x+2, y+1, hops-1, number+str(self.phone[y+1][x+2]))
        ## down 2, left 1
        if ( x - 1 >= 0 and y + 2 <= yMax and self.phone[y+2][x-1] != -1):
            self.traverse(x-1, y+2, hops-1, number+str(self.phone[y+2][x-1]))
        ## down 2, right 1
        if ( x + 1 <= xMax and y + 2 <= yMax and self.phone[y+2][x+1] != -1):
            self.traverse(x+1, y+2, hops-1, number+str(self.phone[y+2][x+1]))
        ## left 2, up 1
        if ( x - 2 >= 0 and y - 1 >= 0 and self.phone[y-1][x-2] != -1):
            self.traverse(x-2, y-1, hops-1, number+str(self.phone[y-1][x-2]))
        ## left 2, down 1
        if ( x - 2 >= 0 and y + 1 >= 0 and self.phone[y+1][x-2] != -1):
            self.traverse(x-2, y+1, hops-1, number+str(self.phone[y+1][x-2]))
        
        
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.seen = dict()
        
        ## print(self.phone)
        x = -1
        y = -1
        for y in range(0, 4):
            for x in range(0, 3):
                ## Left zero side
                if x == 0 and y == 3:
                    continue
                ## Right zero side
                if x == 2 and y == 3:
                    continue
                self.traverse(x, y, N-1, str(self.phone[y][x]))
        
        return len(self.seen) % self.modulo