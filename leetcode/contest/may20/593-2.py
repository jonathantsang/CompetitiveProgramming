class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        import math
        def dist(point1, point2):
            return math.sqrt((point1[1]-point2[1])**2+(point1[0]-point2[0])**2)
        
        def check(value, bo):
            if round(value,2)==round(bo,2):
                return False
            return True
        
        counter = 0
        points = [p1, p2, p3, p4]
        diag = 0
        for i in range(0, len(points)):
            counter = 0
            store = dict()
            saved = dist(points[i], points[0])
            # Find common dist, or fail otherwise
            for p in range(0, len(points)):
                calc = dist(points[i], points[p])
                if calc in store:
                    store[calc] += 1
                    if(store[calc] == 3):
                        return False
                else:
                    store[calc] = 1
            # Check for a key with 2 same length
            good = False
            double = 1
            for k in store.keys():
                if(store[k] == 2):
                    good = True
                elif(store[k] == 1 and diag == 0 and k != 0.0):
                    diag = k
                elif(check(diag, k) and k != 0.0 and store[k] == 1):
                    return False
            if(good == False):
                return False
        return True
        
        
            