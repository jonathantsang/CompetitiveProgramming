class Solution:
    dp = {}
    
    def backwards(self, start, end, steps, mounted):
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
        
        # Can only +1
        if start < end:
            self.backwards(end, end, steps + (end - start), mounted)
        
        if start % 2 == 0:
            ## Can /2 or +1
            if start // 2 <= 2 * end and start >= end:
                mounted = True
            # print(mounted, start // 2, end)
            self.backwards(start // 2, end, steps+1, mounted)
            self.backwards(start+1, end, steps+1, mounted)
        else:
            ## Can only +1
            if start + 1 > 2 * end and (mounted or self.dp[start] > steps):
                return
            self.backwards(start+1, end, steps+1, mounted)
    
    def brokenCalc(self, X: 'int', Y: 'int') -> 'int':
        self.dp = {}
        self.backwards(Y, X, 0, False)
        return self.dp[X]