class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        amt = 0
        cur = 0
        largest = 0
        seen = set() # light num
        seen.add(0)
        for b in light:
            largest = max(largest, b)
            seen.add(b)
            
            if b == cur+1:
                for i in range(cur, len(light)+1):
                    if i in seen:
                        cur = i
                    else:
                        break
            
            if largest == cur:
                amt += 1
            #print(seen)
            #print(largest, cur)
            
        return amt