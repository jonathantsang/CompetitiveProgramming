from heapq import heappop, heappush

class Dijstrka:
    def __init__(self,A):
        self.arr=A

    def run(self):
        # assume edges
        #e[t]->[(adj,distance)...]

        h=[(0,0)]
        seen = set()

        while h:
            dist,node=heappop(h)

            if node in seen:
                continue
            seen.add(node)

            for adj,leng in e[node]:
                heappush(h,(dist+leng,adj))

        return -1
