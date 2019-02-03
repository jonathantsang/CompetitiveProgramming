class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        values = []
        for point in points:
            values.append([math.sqrt(pow(point[0],2) + pow(point[1],2)), point])
        values.sort()
        ans = []
        for i in range(0, K):
            ans.append(values[i][1])
        return ans