class Solution:
    dp = {}
    
    def backwards(self, start, end, steps):
        if start == end:
            if end in self.dp:
                self.dp[end] = min(self.dp[end], steps)
            else:
                self.dp[end] = steps
            return
        
        if end in self.dp and self.dp[end] <= steps:
            return
        if start in self.dp and self.dp[start] <= steps:
            return
        
        if start in self.dp:
            self.dp[start] = min(self.dp[start], steps)
        else:
            self.dp[start] = steps
            
        print(start, end, steps)
        #if end in self.dp:
            #print(self.dp[end])
        # print(self.dp)
        
        if start < end:
            # Keep adding 1s
            self.backwards(end, end, steps + (end - start))
            
        elif end < start:
            self.backwards(end*2, end, steps + (end*2 - start)) # Steps to end * 2
            
    
    def brokenCalc(self, X: 'int', Y: 'int') -> 'int':
        self.dp = {}
        self.backwards(Y, X, 0)
        return self.dp[X]