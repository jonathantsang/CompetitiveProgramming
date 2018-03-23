class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        points = [p1, p2, p3, p4]
        yMax = p1[1]
        yMin = p1[1]
        
        # Coordinates
        topLeft = []
        topRight = []
        botLeft = []
        botRight = []
        
        currentBest = yMax
        inventory = []
        
        # Check maxY
        for point in points:
            if(point[1] > yMax):
                yMax = point[1]
        
        # Add to inv
        for point in points:
            if(point[1] == yMax):
                inventory.append(point) 
                
        print(inventory)
        
        # Exactle two points can have the max Y
        if(len(inventory) != 2):
            return False
        else:
            if(inventory[0][0] > inventory[1][0]):
                topRight = inventory[0]
                topLeft = inventory[1]
            else:
                topRight = inventory[1]
                topLeft = inventory[0]
        inventory = []
        
        # Check yMin
        for point in points:
            if(point[1] < yMin):
                yMin = point[1]
        # Add to inv
        for point in points:
            if(point[1] == yMin):
                inventory.append(point)
                
        # Exactle two points can have the max Y
        if(len(inventory) != 2):
            return False
        else:
            if(inventory[0][0] > inventory[1][0]):
                botRight = inventory[0]
                botLeft = inventory[1]
            else:
                botRight = inventory[1]
                botLeft = inventory[0]
        inventory = []
        
        # Calc sides
        l1 = abs(topRight[1]-botRight[1])
        l2 = abs(topLeft[1]-botLeft[1])
        w1 = abs(botLeft[0]-botRight[0])
        w2 = abs(topLeft[0]-topRight[0])
        return (l1 == l2 and w1 == w2)