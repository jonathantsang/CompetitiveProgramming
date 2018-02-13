class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        total = 0
        if(len(flowerbed) == 1):
            if(flowerbed[0] == 0):
                total += 1
                return total >= n
            else:
                return total >= n
        last = flowerbed[0]
        i = 0
        while(i < len(flowerbed)):
            if(flowerbed[i] == 0):
                if(i-1 < 0):
                    if(flowerbed[i+1] == 0):
                        total += 1
                        if(i+1 < len(flowerbed)):
                            i += 1
                elif(i+1 >= len(flowerbed)):
                    if(flowerbed[i-1] == 0):
                        total += 1
                        if(i+1 < len(flowerbed)):
                            i += 1
                
                elif(flowerbed[i-1] == 0 and flowerbed[i+1] == 0):
                    total += 1
                    if(i+1 < len(flowerbed)):
                        i += 1
            i += 1
        return total >= n