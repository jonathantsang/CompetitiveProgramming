import statistics
import heapq

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        m = arr[(len(arr)-1)//2]
        #print(m)
        h = []
        for v in arr:
            h.append((abs(v-m), v))
        heapq.heapify(h)
        largest = heapq.nlargest(k, h)

        return list(map(lambda x: x[1], largest))
