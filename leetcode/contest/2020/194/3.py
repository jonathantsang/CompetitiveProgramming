class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        dry = [] # place to dry
        rained = defaultdict(int) # lake -> rained index
        ans = []
        for i, lake in enumerate(rains):
            if lake == 0:
                dry.append(i)
                ans.append(1)
            else:
                if lake in rained:
                    if len(dry) <= 0:
                        return []
                    rainedindex = rained[lake]
                    chosen = -1
                    for j, dryindex in enumerate(dry):
                        if dryindex > rainedindex:
                            dry.pop(j)
                            chosen = dryindex
                            break
                    if chosen == -1:
                        return []
                    ans[chosen] = lake
                    #print(ans)
                    rained[lake] = i
                else:
                    rained[lake] = i
                ans.append(-1)
        return ans
                    
