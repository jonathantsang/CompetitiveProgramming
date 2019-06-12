class Solution:
    
    def daysforcapacity(self, weights, capacity):
        cur = 0
        days = 0
        for i, c in enumerate(weights):
            if cur + c <= capacity:
                cur += c
            else:
                days += 1
                cur = c
        if cur != 0: ## Last day
            days += 1
        return days
    
    
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        totalweight = 0
        for v in weights:
            totalweight += v
        lowerc = max(weights) # Since each capacity must be able to ship the max weight item
        higherc = totalweight
        
        while(higherc -lowerc != 1):
            midc = (higherc + lowerc) // 2
            days = self.daysforcapacity(weights, midc)
            # print(days, lowerc, higherc, midc)
            if days <= D:
                higherc = midc
            else:
                lowerc = midc
            # print(lowerc, higherc)
                
        d1 = self.daysforcapacity(weights, higherc)
        d2 = self.daysforcapacity(weights, lowerc)
        # print(higherc, lowerc, d1, d2)
        if d2 <= D:
            return lowerc
        else:
            return higherc