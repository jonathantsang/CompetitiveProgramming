import heapq

class Solution:
    def solve(self, weights, values, capacity):
        # Write your code here
        best = []
        for i in range(len(weights)):
            best.append((-values[i] /  weights[i], values[i], weights[i]))
        heapq.heapify(best)
        #print(best)
        
        total = 0
        while len(best) > 0 and capacity > 0:
            score, val, weight = heapq.heappop(best)
            percent = capacity / weight
            if percent >= 1:
                capacity -= weight
                total += val
            else:
                capacity -= weight * percent
                total += val * percent
                break
        return int(total)