class Solution:
    def traverse(self, node, time, timelimit, target, probability):        
        if time > timelimit:
            return
        if node in self.seen:
            return
        self.seen.add(node)
        #print(node, probability)
        if node == target and time == timelimit:
            self.prob[target] = probability    
            return
        else:
            if node in self.children:
                validC = len(self.children[node]) # need the ones not already seen
                for c in self.children[node]:
                    if c in self.seen:
                        validC -= 1                
                
                # jump on same target edge case
                if node == target and time < timelimit and validC == 0:
                    self.prob[node] = probability
                    return
                if validC == 0:
                    return
                
                for c in self.children[node]:
                    self.traverse(c, time+1, timelimit, target, probability / validC)
            else:
                self.prob[node] = probability
        
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        self.prob = {target: 0} # n -> probability
        self.children = {} # n -> [child nodes]
        self.seen = set() # n
        
        for e in edges:
            if e[0] in self.children:
                self.children[e[0]].append(e[1])
            else:
                self.children[e[0]] = [e[1]]
            if e[1] in self.children:
                self.children[e[1]].append(e[0])
            else:
                self.children[e[1]] = [e[0]]

        self.traverse(1, 0, t, target, 1)
        #print(self.prob)
        return self.prob[target]