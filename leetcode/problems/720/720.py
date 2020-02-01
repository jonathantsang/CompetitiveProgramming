class Solution:
    def built(self, w, v):
        if len(w) + 1 != len(v):
            return False
        onemiss = False
        
        if len(w) == 1:
            return v[0] == w or v[1] == w
        
        for i, c in enumerate(v):
            if onemiss and i >= len(w):
                return v[i] == w[i-1]
            if i >= len(w):
                return True
            if onemiss == False and v[i] != w[i]:
                onemiss = True
            elif onemiss == True and v[i] != w[i-1]:
                return False
            else:
                # same fine
                pass
        return onemiss
    
    def longestWord(self, words: List[str]) -> str:
        best = []
        edges = {} # Key: word, Value: array of possible transform word
        end = []
        for w in words:
            for v in words:
                if w == v:
                    continue
                else:
                    if self.built(w, v):
                        if w in edges:
                            edges[w].append(v)
                        else:
                            edges[w] = [v]
        #print(edges)
        smallest = float('inf')
        for w in words:
            smallest = min(smallest, len(w))
        for w in words:
            if len(w) == smallest:
                best.append(w)
        #print(best)
        
        while len(best) > 0:
            val = best.pop(0)
            if val not in edges:
                end.append(val)
                continue
            for p in edges[val]:
                best.append(p)
        #print(end)
        
        longest = -1
        for w in end:
            longest = max(len(w), longest)
        
        ans = []
        for w in end:
            if len(w) == longest:
                ans.append(w)
        ans.sort()
        
        return ans[0]