class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        ht = dict()
        ## Only gets maximum of this amount since they have to be equal
        equalNum = len(candies) / 2
        count = 0
        for i in range(0, len(candies)):
            if(equalNum <= 0):
                break
            elif(candies[i] not in ht):
                ht[candies[i]] = 1
                count += 1
                equalNum -= 1
        return count