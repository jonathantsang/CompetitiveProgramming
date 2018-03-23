class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        ## Includes start, not end
        start = 0
        end = 1
        lengMax = 0
        i = 0
        while(i < len(word1)):
            s = 0
            e = 1
            maxi = 0
            j = 0
            while(j < len(word2)):
                if(word1[i] == word2[j]):
                    e += 1
                    maxi += 1
                    if(i + 1 >= len(word1)):
                        break
                    else:
                        i += 1
                else:
                    if(maxi > lengMax):
                        lengMax = maxi
                        start = s
                        end = e
                j += 1
            if(maxi > lengMax):
                lengMax = maxi
                start = s
                end = e
            i +=1
        original = len(word1)
        ## Special Case
        if(word1 == word2):
            return 0
        accounted = lengMax
        need = len(word2)
        return abs(original - accounted) + abs(need - accounted)