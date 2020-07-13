class Solution:    
    def getMinDistSum(self, P: List[List[int]]) -> float:
        def allDist(p):
            ix,iy = p
            
            def dist(x,y,x2,y2):
                return sqrt((x-x2)**2+(y-y2)**2)
            
            total = 0
            for x,y in P:
                total += dist(ix,iy,x,y)
            
            return total

        N = len(P)
        bestpointsofar = [0,0]
        for x,y in P:
            bestpointsofar[0]+=x
            bestpointsofar[1]+=y
        
        bestpointsofar[0] /= N
        bestpointsofar[1] /= N
        
        minsofar = allDist(bestpointsofar)
        
        # calculate best point
        k = 0
        while k < N:
            for i in range(N):
                if i == k:
                    break
                otherpoint = P[i]
                otherdist = allDist(otherpoint)
                if otherdist < minsofar:
                    minsofar = otherdist
                    bestpointsofar = otherpoint
            k+=1
            
        value = 1000
        valid = 0
        
        # approximate on 10^5
        lower = 0.00001
        while value > lower:
            valid = 0
            
            for x,y in [(-1,0),(0,1),(1,0),(0,-1)]:
                otherpoint = [bestpointsofar[0]+value*x, bestpointsofar[1]+value*y]
                otherdist = allDist(otherpoint)
                #print(otherdist, minsofar)
                
                if otherdist < minsofar:
                    minsofar = otherdist
                    bestpointsofar = otherpoint
                    valid = 1
                    break
                    
            if valid == 0:
                value /= 2
        
        return minsofar