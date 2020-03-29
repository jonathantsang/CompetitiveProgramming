import heapq

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        modulo = 10**9+7
        best = 0
        efficiencies = {} # efficiency # -> heap [possible speed #]
        for i in range(0, len(efficiency)):
            if efficiency[i] in efficiencies:
                efficiencies[efficiency[i]].append(speed[i])
            else:
                efficiencies[efficiency[i]] = [speed[i]]
        # sort each one
        m_e = max(efficiencies)
        for e in efficiencies:
            heapq.heapify(efficiencies[e])
        best_h = []
        heapq.heapify(best_h)
        for i in range(1, m_e+1):
            total = 0
            if len(best_h) == k:
                if i not in efficiencies:
                    continue
                # just check new row
                for value in efficiencies[i]:
                    if value > best_h[0]:
                        heapq.heapushpop(best_h, value)
                total = sum(best_h)
            else:
                for j in range(0, k):
                    cur_b = -float('inf')
                    idx = -1
                    for e in efficiencies:
                        if e >= i:
                            if len(efficiencies[e]) > 0 and efficiencies[e][0] > cur_b:
                                cur_b = efficiencies[e][0]
                                idx = e
                    if idx == -1:
                        # unable to find valid for max efficiency
                        break
                    val = heapq.heappop(efficiencies[idx])
                    total += val
                    heapq.heappush(best_h, val)
            best = max(best, total * i)
            print(best)
        return best % modulo