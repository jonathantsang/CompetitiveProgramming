class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        heap = []
        for v in c:
            heap.append((c[v], v))

        heapq.heapify(heap)

        for _ in range(k):
            count, v = heapq.heappop(heap)
            if count > 1:
                count -= 1
                heapq.heappush(heap, (count, v))

        return len(Counter(heap))
