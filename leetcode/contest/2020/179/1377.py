import collections

class Solution:
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
        
        if edges == []:
            return 1.0

        queue = collections.deque()
        queue.append((1, 0, 1)) # (node, time, probability so far)
        
        while len(queue) > 0:
            # print(queue)
            val = queue.popleft()
            
            node = val[0]
            time = val[1]
            probability = val[2]
            
            if time > t:
                continue
            
            if node in self.seen:
                continue
            self.seen.add(node)
            
            if node == target and time == t:
                self.prob[target] = probability
                break
            else:
                if node in self.children:
                    validC = len(self.children[node])
                    for c in self.children[node]:
                        if c in self.seen:
                            validC -= 1
                    if validC == 0 and node == target:
                        self.prob[target] = probability
                        break
                    if validC == 0:
                        continue
                    for c in self.children[node]:
                        if c not in self.seen:
                            queue.append((c, time+1, probability / validC))
        return self.prob[target]