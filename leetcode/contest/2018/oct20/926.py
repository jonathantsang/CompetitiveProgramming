class Solution(object):
    
    seen = dict()
    best = 9999999999
    
    def recurse(self, S, start, ops):
        if S in self.seen:
            return
        self.seen[S] = 1
        
        one = False
        mono = True
        ## print(S)
        for i in range(0, len(S)):
            if S[i] == '0' and one == True:
                ## Fail
                mono = False
                break
            elif S[i] == '1':
                one = True
        if mono == True:
            self.best = min(self.best, ops)
        
        for i in range(start, len(S)):
            char = '1'
            if S[i] == '1':
                char = '0'
            else:
                char = '1'
            self.recurse(S[0:i] + char + S[i+1:], i, ops+1)
    
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        self.seen = dict()
        self.best = 9999999999
        self.recurse(S, 0, 0)
        return self.best
        