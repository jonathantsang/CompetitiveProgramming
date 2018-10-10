class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        count = dict()
        for val in deck:
            if val in count:
                count[val] += 1
            else:
                count[val] = 1
        lowestVal = 99999999999
        for val in count:
            lowestVal = min(count[val], lowestVal)
            if count[val] < 2:
                return False
        for i in range(2, lowestVal+1):
            worksAll = True
            for val in count:
                if count[val] % i != 0:
                    worksAll = False
                    break
            if worksAll:
                return True
        return False