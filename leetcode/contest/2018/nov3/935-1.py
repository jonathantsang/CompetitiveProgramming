class Solution(object):
    graph = dict()
    total = dict()
    modulo = 1000000000 + 7
    
    def traverse(self, start, cur, N):
        if N == 0:
            if start in self.total:
                self.total[start] += 1
            else:
                self.total[start] = 1
            return
        ## For each adjacent
        for i in range(0, len(self.graph[cur])):
            self.traverse(start, self.graph[cur][i], N-1)
    
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.graph = dict() ## key: number, val: array of adjacent vals
        self.graph[0] = [4,6]
        self.graph[1] = [6,8]
        self.graph[2] = [7,9]
        self.graph[3] = [4,8]
        self.graph[4] = [0,3,9]
        self.graph[5] = []
        self.graph[6] = [0,1,7]
        self.graph[7] = [6,2]
        self.graph[8] = [1,3]
        self.graph[9] = [2,4]
        self.total = dict() ## All multiply by 2 except 0 value
        use = [2, 4, 5]
        for i in use: ## 0 to 5
            self.traverse(i, i, N-1)
            print (i, self.total)
        combined = 0
        print (self.total)
        combined += ((self.total[2] + self.total[4]) / 2 * 4) % self.modulo
        for key in self.total:
            if key == 1:
                self.total[key] *= 4
            if key == 2:
                self.total[key] *= 2
            if key == 4:
                self.total[key] *= 3
            combined += self.total[key]
            combined %= self.modulo
        
        return combined