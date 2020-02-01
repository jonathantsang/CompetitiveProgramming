import heapq

class Solution(object):
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type num_wanted: int
        :type use_limit: int
        :rtype: int
        """
        maxheap = []
        for i in range(0, len(values)):
            heapq.heappush(maxheap, (-values[i], labels[i]))
        
        best = 0
        i = 0
        used = {} # Label -> Amount used
        while i < num_wanted and len(maxheap) > 0:
            p = heapq.heappop(maxheap)
            # print(p)
            if p[1] in used and used[p[1]] >= use_limit:
                continue
            else:
                best += -p[0]
                i += 1
                if p[1] in used:
                    used[p[1]] += 1
                else:
                    used[p[1]] = 1
        return best