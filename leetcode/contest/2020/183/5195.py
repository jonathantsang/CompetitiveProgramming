class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        s = []
        
        # largest
        vals = [[-a, 'a'], [-b, 'b'], [-c, 'c']]
        vals.sort()
        prior = None
        twoprior = None
        while vals[0][0] < 0:
            #print(vals, prior, twoprior)
            if prior == twoprior and prior == vals[0][1]:
                if vals[1][0] < 0:
                    s.append(vals[1][1])
                    vals[1][0] += 1
                    
                    twoprior = prior
                    prior = vals[1][1]
                    vals.sort()

                else:
                    break
            else:
                s.append(vals[0][1])
                vals[0][0] += 1
                
                twoprior = prior
                prior = vals[0][1]
                vals.sort()
            
        return "".join(s)
            