class Solution:
    def traverse(self, node, goto, informTime, totalTime):
        # no more child nodes to go to
        if node not in goto:
            self.largest = max(self.largest, totalTime)
        else:
            for child in goto[node]:
                self.traverse(child, goto, informTime, totalTime+informTime[node])
                
        
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        self.largest = 0
        goto = {} # node -> [child nodes]
        for i in range(0, len(manager)):
            n = manager[i]
            if n in goto:
                goto[n].append(i)
            else:
                goto[n] = [i]
                
        self.traverse(headID, goto, informTime, 0)
        return self.largest