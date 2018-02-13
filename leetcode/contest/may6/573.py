class Solution(object):
    
    ## Finds the distance from squirrel's position to the other position
    def findDistance(self, sPos, objPos):
        return abs(sPos[0] - objPos[0]) + abs(sPos[1] - objPos[1])
        
    ## Returns index of the closest nut
    def findClosestNut(self, sPos, listofNuts):
        lowest = 999999
        lowestPos = None
        index = 0
        for i in range(0, len(listofNuts)):
            calcDistance = self.findDistance(sPos, listofNuts[i])
            if(calcDistance < lowest):
                ## Save the position and the lowest distance
                lowestPos = listofNuts[i]
                lowest = calcDistance
                index = i
        return index
    
    ## Returns index of the furthest nut from the tree
    ## Used on the first search
    def findOptimalNutFromTree(self, tPos, sPos, listofNuts):
        highest = -99999999
        highestPos = None
        index = 0
        for i in range(0, len(listofNuts)):
            distFromTree = self.findDistance(tPos, listofNuts[i])
            distFromS = self.findDistance(sPos, listofNuts[i])
            optimal = distFromTree - distFromS
            if(optimal > highest):
                ## Save the position and the lowest distance
                highestPos = listofNuts[i]
                highest = optimal
                index = i
        return index
    
    def minDistance(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """
        ## On the first move, you want to go to the furthest nut to avoid the number of steps later
        totalMovement = 0
        for i in range(0, len(nuts)):
            
            ## On first search, look for furthest nut from tree
            if(i == 0):
                closestNut = self.findOptimalNutFromTree(tree, squirrel, nuts)
            else:
                ## Find Closest Nut
                closestNut = self.findClosestNut(squirrel, nuts)
            
            ## closestNut is right now an index    
            closeNutPos = nuts[closestNut]
            ## Remove the nut from the array
            del nuts[closestNut]
            
            ## Squirrel moves to the nut
            totalMovement += self.findDistance(squirrel, closeNutPos)
            squirrel = closeNutPos
            ## Squirrel moves to the tree
            totalMovement += self.findDistance(squirrel, tree)
            squirrel = tree
        return totalMovement
            
            