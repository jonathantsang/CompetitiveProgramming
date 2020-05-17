import math

class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        best = 1 # at worst can get one point in the circle

        def checkCircle(x, y, i, j):
            count = 0
            for k, p in enumerate(points):
                if k == i or k == j:
                    count += 1 # on edge of i and j
                    continue
                px = p[0]
                py = p[1]
                if ((px - x)**2 + (py - y)**2) <= r**2:
                    count += 1
            #print(x, y, " has ", count)
            #print(i, j)
            return count

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1 = points[i][0]
                x2 = points[j][0]
                y1 = points[i][1]
                y2 = points[j][1]
                x3 = (x1+x2)/2
                y3 = (y1+y2)/2

                # construct circle from two points
                q = math.sqrt((x2-x1)**2 + (y2-y1)**2)

                # x = x3 + sqrt(r^2-(q/2)^2)*(y1-y2)/q
                # y = y3 + sqrt(r^2-(q/2)^2)*(x2-x1)/q
                if r**2-(q/2)**2 < 0:
                    continue # no circle between in radius r
                cx = x3 + math.sqrt(r**2-(q/2)**2)*(y1-y2)/q
                cy = y3 + math.sqrt(r**2-(q/2)**2)*(x2-x1)/q
                best = max(checkCircle(cx, cy, i, j), best)

                if r**2-(q/2)**2 < 0:
                    continue # no circle between in radius r
                # x = x3 - sqrt(r^2-(q/2)^2)*(y1-y2)/q
                # y = y3 - sqrt(r^2-(q/2)^2)*(x2-x1)/q
                cx = x3 - math.sqrt(r**2-(q/2)**2)*(y1-y2)/q
                cy = y3 - math.sqrt(r**2-(q/2)**2)*(x2-x1)/q
                best = max(checkCircle(cx, cy, i, j), best)

        return best
