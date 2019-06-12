class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        A = 0
        B = 0
        cost = 0
        swapcosts = [] # Each index is swap cost for person i, index i, and 'A' or 'B'
        for i, person in enumerate(costs):
            # Cost of A < B
            if person[0] < person[1]:
                A += 1
                cost += person[0]
                swapcosts.append([abs(person[0]-person[1]), i, 'A'])
            else:
                B += 1
                cost += person[1]
                swapcosts.append([abs(person[0]-person[1]), i, 'B'])
        # Compare A and B
        diff = max(A, B) - (len(costs) / 2)
        swapcosts.sort() # Sort by the swap costs
        
        rid = 'A'
        if A < B:
            rid = 'B'
        count = 0
        #print(swapcosts)
        #print(A, B, diff)
        #print(cost)
        for sc in swapcosts:
            if count == diff:
                break
            if sc[2] == rid:
                cost += sc[0]
                count += 1
        return cost